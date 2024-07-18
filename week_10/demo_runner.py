import os
import random
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

# Load environment variables
load_dotenv(override=True)

class OpenAIChatClient:
    def __init__(self, prompt):
        load_dotenv(override=True)
        self._client = self._get_client()
        self._prompt = prompt

    def _get_client(self):
        client = AzureOpenAI(
            api_version=os.environ.get("AZURE_OPENAI_API_VERSION"),
            azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
            api_key=os.environ.get("AZURE_OPENAI_KEY"),
        )
        return client

    def _get_completion(self, user_message):
        messages = [
            {"role": "system", "content": self._prompt},
            {"role": "user", "content": user_message},
        ]

        chat_completion = self._client.chat.completions.create(
            messages=messages,
            model=os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME"),
            max_tokens=10,
            temperature=.1
        )
        return chat_completion

    def _parse_completion(self, chat_completion):
        return chat_completion.choices[0].message.content

    def get_completion(self, subject):
        chat_completion = self._get_completion(subject)
        completion_content = self._parse_completion(chat_completion)
        return completion_content

randomizer_chat_client = OpenAIChatClient(
    """
    You generate random responses for the following field.
    Your responses always somehow relate to Santa Claus.
    Your response should be at most 5 words.
    """
)

endpoint = os.environ.get("FORM_RECOGNIZER_ENDPOINT")
key = os.environ.get("FORM_RECOGNIZER_KEY")

# Initialize Azure Document Analysis Client
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

image_path = r"week_10\forms\employment_application.png"
with open(image_path, "rb") as f:
    document = f.read()

poller = document_analysis_client.begin_analyze_document("prebuilt-document", document)
result = poller.result()

# Load the image
image = Image.open(image_path)
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()  # You can replace this with a path to a TTF file and use ImageFont.truetype


# Find all bounding boxes and generate responses
key_value_pairs = []
for kv_pair in result.key_value_pairs:
    if kv_pair.key and kv_pair.value and kv_pair.value.bounding_regions:
        if kv_pair.value.content.startswith(":") and kv_pair.value.content.startswith(":"):
            continue # skip boxes.
        key_content = kv_pair.key.content
        bounding_box = kv_pair.value.bounding_regions[0].polygon
        response = randomizer_chat_client.get_completion(key_content)
        key_value_pairs.append((key_content, bounding_box, response))

# Draw polygons and add text
for key, bounding_box, response in key_value_pairs:
    polygon = [(point.x, point.y) for point in bounding_box]
    draw.polygon(polygon, fill="white")
    draw.text((polygon[0][0], polygon[0][1]), response, fill="black", font=font)

# Display the final image
image.show()

# Optionally, save the modified image
image.save(r"week_10\forms\modified_employment_application.png")
