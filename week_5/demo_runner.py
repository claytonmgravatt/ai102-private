# Standard library imports
import os

# Third-party imports
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

# Load environment variables
load_dotenv(override=True)

# Azure QA Service configuration
endpoint = os.environ.get("AZURE_LANGUAGE_ENDPOINT")
api_key = os.environ.get("AZURE_LANGUAGE_API_KEY")
credential = AzureKeyCredential(api_key)
question_answering_client = QuestionAnsweringClient(endpoint=endpoint, credential=credential)
project = os.environ.get("AZURE_LANGUAGE_CUSTOM_QA_PROJECT")
deployment = "production"

# Flask application setup
app = Flask(__name__)

@app.route("/")
def home():
    """ Serve the main layout HTML. """
    return render_template("layout.html")

@app.route("/message", methods=["POST"])
def message():
    """ Endpoint to receive messages and respond with answers. """
    user_input = request.json["message"]
    response = process_message(user_input)
    return jsonify({"message": response})

def process_message(input_text):
    """ Process the user message by getting answers from Azure QA service. """
    response = question_answering_client.get_answers(
        question=input_text,
        project_name=project,
        deployment_name=deployment,
        confidence_threshold=0.5,
    )
    answer = response.answers[0].answer
    return answer

if __name__ == "__main__":
    # Start the Flask application with debugging enabled
    app.run(debug=True)
