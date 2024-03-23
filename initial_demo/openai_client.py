import requests
import os
import json

from dotenv import load_dotenv
from openai import AzureOpenAI
from PIL import Image

class OpenAIImageClient:
    def __init__(self):
        load_dotenv(override=True)
        self._client = self._get_client()
        self.image_dir = 'images'

    def _get_client(self):
        client = AzureOpenAI(
            api_version=os.environ.get("AZURE_OPENAI_DALLE_API_VERSION"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_KEY"),
        )
        return client
    
    def _get_image_url(self, user_prompt: str):
        print('Generating an image...')
        response = self._client.images.generate(
            model=os.environ.get('AZURE_OPENAI_DALLE_DEPLOYMENT_NAME'), 
            prompt=user_prompt,
            n=1
        )
        image_url = json.loads(response.model_dump_json())['data'][0]['url']
        return image_url
    
    def _save_image(self, image_url:str):
        if not os.path.isdir(self.image_dir):
            os.mkdir(self.image_dir)
        image_path = os.path.join(self.image_dir, 'generated_image.png')
        generated_image = requests.get(image_url).content  # download the image

        with open(image_path, "wb") as image_file:
            image_file.write(generated_image)

        image = Image.open(image_path)
        image.show()

    def get_image(self, user_prompt):
        image_url = self._get_image_url(user_prompt)
        self._save_image(image_url)
    

class OpenAIChatClient:
    def __init__(self):
        load_dotenv(override=True)
        self._client = self._get_client()
        self.joke_prompt = 'You are a chatbot that tells jokes. Do not tell rude jokes.' # maybe refactor this to just prompt, joke is a child class

    def _get_client(self):
        client = AzureOpenAI(
            api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_KEY"),
        )
        return client
    
    def _get_completion(self, system_message, user_message):
        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": user_message,
            },
        ]

        chat_completion = self._client.chat.completions.create(
            messages=messages,
            model=os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME")
        )
        return chat_completion
    
    def _parse_completion(self, chat_completion):
        chat_completion
        return chat_completion.choices[0].message.content
    
    def get_joke(self, subject):
        chat_completion = self._get_completion(self.joke_prompt, subject)
        completion_content = self._parse_completion(chat_completion)
        return completion_content
    
### Example usage
if __name__ == '__main__':
    chat_client = OpenAIChatClient()
    image_client = OpenAIImageClient()
    #joke = chat_client.get_joke('Tell me a joke about gnomes.')
    #print(joke)

    image_client.get_image('Show me a rococo painting of a raccoon.')