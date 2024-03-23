import os
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

class IntentClient:

    def __init__(self):
        load_dotenv(override=True)
        self.project = os.environ.get('AZURE_CLU_PROJECT')
        self.deployment = os.environ.get('AZURE_CLU_DEPLOYMENT')
        self._client = self._get_client()

    def _get_client(self):
        endpoint = os.environ.get('AZURE_LANGUAGE_ENDPOINT')
        api_key = os.environ.get('AZURE_LANGUAGE_API_KEY')
        credential = AzureKeyCredential(api_key)
        client = ConversationAnalysisClient(endpoint, credential)
        return client
    
    def get_intent(self, utterance: str):
        result = self._client.analyze_conversation(
            task={
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "participantId": "1",
                        "id": "1",
                        "modality": "text",
                        "language": "en",
                        "text": utterance
                    },
                    "isLoggingEnabled": False
                },
                "parameters": {
                    "projectName": self.project,
                    "deploymentName": self.deployment,
                    "verbose": True
                }
            }
        )
        intent = result["result"]["prediction"]["topIntent"]
        return intent

### Example usage:
if __name__ == '__main__':
    intent_client = IntentClient()
    query = 'Tell me a joke about gnomes.'

    intent = intent_client.get_intent(query)
    print(intent)

