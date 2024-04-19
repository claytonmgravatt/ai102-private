import os

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

load_dotenv(override=True)

endpoint = os.environ.get("AZURE_LANGUAGE_ENDPOINT")
api_key = os.environ.get("AZURE_LANGUAGE_API_KEY")
credential = AzureKeyCredential(api_key)

conversation_analysis_client = ConversationAnalysisClient(
    endpoint=endpoint, credential=credential
)

project = "ai-102-demo-bank-proj"
deployment = "bank-prod"

app = Flask(__name__)

# Hardcoded "database" information
account = {
    "account number": "12345678",
    "name": "Clayton",
    "email": "clayton@money.com",
    "savings": 0.02,
    "checking": 0.38,
    "meg":1_000_000
}


def analyze_conversation(utterance):
    result = conversation_analysis_client.analyze_conversation(
        task={
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": utterance,
                },
                "isLoggingEnabled": False,
            },
            "parameters": {
                "projectName": project,
                "deploymentName": deployment,
                "verbose": True,
            },
        }
    )

    intent = result["result"]["prediction"]["topIntent"]
    entities = result["result"]["prediction"]["entities"]

    print(intent, entities)

    return intent, entities

def get_response_for_single_expected_entity(entities, expected_keys, expected_entity_type):
    response_specific_entities = [
        entity["text"].lower()
        for entity in entities
        if entity["category"] == expected_entity_type
    ]
    if response_specific_entities:
        response = {entity: account[entity] for entity in response_specific_entities}
    else:
        response = {key: account[key] for key in expected_keys}
    return response

def get_account_info(entities):
    expected_keys = ["account number", "email", "name"]
    expected_entity_type='AccountInfoType'
    account_fields = get_response_for_single_expected_entity(entities, expected_keys, expected_entity_type)
    return " | ".join([f"{key.title()}: {value}" for key, value in account_fields.items()])

def get_balance(entities):
    expected_keys = ["checking", "savings"]
    expected_entity_type='BalanceType'
    balances = get_response_for_single_expected_entity(entities, expected_keys, expected_entity_type)
    return " | ".join([f"Balance in {account_name.title()} account: ${balance}" for account_name, balance in balances.items()])

def transfer(entities):
    def get_first_entity_of_type(entities, entity_type):
        filtered_entities =  [
        entity["text"].lower()
        for entity in entities
        if entity["category"] == entity_type
    ]
        if filtered_entities:
            return filtered_entities[0]
        else:
            raise ValueError(f'Missing {entity_type}.')
        
    from_entity = get_first_entity_of_type(entities, 'SendFrom')
    to_entity = get_first_entity_of_type(entities, 'SendTo')
    amount = get_first_entity_of_type(entities, 'SendAmount').replace('$','')

    account[from_entity] -= float(amount)
    account[to_entity] += float(amount)

    return f"Transferred ${amount} from {from_entity} to {to_entity}. Hope that's what you wanted."


def process_user_input(utterance):
    intent, entities = analyze_conversation(utterance)

    if intent == "GetAccountInfo":
        response = get_account_info(entities)
    elif intent == "GetBalance":
        response = get_balance(entities)
    elif intent == "TransferMoney":
        response = transfer(entities)
    else:
        response = "I'm sorry, what?"

    print(response)

    return response


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.get_json()
        user_input = data["user_input"]
        print("Received input:", user_input)
        response = process_user_input(user_input)
        return jsonify({"response": response, "account":account})
    else:
        return render_template("index.html", account=account)


if __name__ == "__main__":
    app.run(debug=True)
