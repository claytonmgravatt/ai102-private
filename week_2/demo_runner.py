import json
import os

from flask import Flask, render_template, request
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

load_dotenv(override=True)


image_data_path = "image_tags.json"
image_dir = r"static\images"

regenerate_tags_on_launch = True


def regenerate_tags():
    endpoint = os.environ.get("AZURE_VISION_ENDPOINT")
    api_key = os.environ.get("AZURE_VISION_API_KEY")
    credential = AzureKeyCredential(api_key)

    image_analysis_client = ImageAnalysisClient(endpoint, credential)

    images = os.listdir(image_dir)
    image_tags = []

    for image_path in images:
        with open(os.path.join(image_dir, image_path), "rb") as image_data:
            image_analysis = image_analysis_client.analyze(
                image_data=image_data, visual_features=["TAGS"]
            )

            image_tags.append(
                {
                    "filename": image_path,
                    "tags": [
                        tag["name"] for tag in image_analysis["tagsResult"]["values"]
                    ],
                    "metadata": {
                        "width": image_analysis["metadata"]["width"],
                        "height": image_analysis["metadata"]["height"],
                    },
                }
            )

    with open(image_data_path, "w") as outfile:
        json.dump(image_tags, outfile, indent=4)

    print("Image tags saved to image_tags.json")


if regenerate_tags_on_launch:
    regenerate_tags()

# Load image tags and metadata
with open(image_data_path) as f:
    image_data = json.load(f)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    selected_tag = request.args.get("tag")
    if selected_tag:
        # Filter images by the selected tag
        filtered_images = [
            image for image in image_data if selected_tag in image["tags"]
        ]
    else:
        # If no tag is selected, show all images
        filtered_images = image_data

    # Extract unique tags for sidebar or dropdown
    tags = set(tag for image in image_data for tag in image["tags"])

    return render_template(
        "index.html",
        images=filtered_images,
        tags=sorted(tags),
        selected_tag=selected_tag,
    )


if __name__ == "__main__":
    app.run(debug=True)
