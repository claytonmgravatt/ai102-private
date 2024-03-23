import os
import json

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv


load_dotenv(override=True)
endpoint = os.environ.get("AZURE_VISION_ENDPOINT")
api_key = os.environ.get("AZURE_VISION_API_KEY")
credential = AzureKeyCredential(api_key)

image_analysis_client = ImageAnalysisClient(endpoint, credential)

image_dir = 'images'
images = [os.path.join(image_dir, image) for image in os.listdir(image_dir)]
image_tags = []

for image_path in images:
    with open(os.path.join(image_dir, image_path), 'rb') as image_data:
        image_analysis = image_analysis_client.analyze(
            image_data=image_data, visual_features=['TAGS']
        )

        image_tags.append({
            "filename": image_path,
            "tags": [tag['name'] for tag in image_analysis['tagsResult']['values']],
            "metadata": {
                "width": image_analysis['metadata']['width'],
                "height": image_analysis['metadata']['height']
            }
        })

with open('image_tags.json', 'w') as outfile:
    json.dump(image_tags, outfile, indent=4)

print("Image tags saved to image_tags.json")


