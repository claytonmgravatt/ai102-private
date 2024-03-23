from intent_client import IntentClient
from openai_client import OpenAIChatClient, OpenAIImageClient
from speech_client import AzureSpeechClient

chat_client = OpenAIChatClient()
image_client = OpenAIImageClient()
intent_client = IntentClient()
speech_client = AzureSpeechClient()

#assert intent_client.get_intent('Paint me a picture of a frog.') == 'MakePicture'
#assert intent_client.get_intent('Tell me a joke about a frog.') == 'GetJoke'

user_request = speech_client.get_text_from_speech()
print(f"{user_request=}")

intent = intent_client.get_intent(user_request)

if intent == 'GetJoke':
    joke = chat_client.get_joke(user_request)
    print(f"{joke=}")
    speech_client.get_speech_from_text(joke)

if intent == 'MakePicture':
    image_client.get_image(user_request)


