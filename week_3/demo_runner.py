import os
import requests
import json
import matplotlib.pyplot as plt

from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

# Load environment variables
load_dotenv(override=True)
endpoint = os.environ.get("AZURE_VISION_ENDPOINT")
api_key = os.environ.get("AZURE_VISION_API_KEY")
model_name = 'basickittyobject'
api_version = "2023-02-01-preview"

# Setup for saving detected objects
detected_objects_info = []

# Prepare the headers for the API request
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/octet-stream"
}

# Loop through all images in the "evidence" folder
evidence_folder = 'evidence'
image_files = [file for file in os.listdir(evidence_folder) if file.lower().endswith('jpg')]

detected_objects_info_path = 'detected_objects_info.json'
if not os.path.exists(detected_objects_info_path):
    for idx, image_file in enumerate(image_files):
        image_path = os.path.join(evidence_folder, image_file)
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # Sending the request to Azure Vision API
        url = f"{endpoint}/computervision/imageanalysis:analyze?model-name={model_name}&api-version={api_version}"
        response = requests.post(url, headers=headers, data=image_data)
        response_data = json.loads(response.text)

        # Save detected objects information
        detected_objects_info.append(response_data)

    # Optionally, save detected objects information to a file
    with open(detected_objects_info_path, "w") as f:
        json.dump(detected_objects_info, f, indent=4)

with open(detected_objects_info_path, 'r') as f:
    detected_objects_info = json.load(f)


# Calculate grid size for subplots
total_images = len(image_files)
cols = 3
rows = total_images // cols + (total_images % cols > 0)

# Prepare subplot
fig, axs = plt.subplots(nrows=rows, ncols=cols, figsize=(20, 10 * rows))
axs = axs.flatten()  # Flatten the array for easy iteration

table_bounding_box = ((1550, 900), (3300, 1600))

def bounding_boxes_intersect(box1, box2):
    # Unpack the coordinates
    (x1_min, y1_min), (x1_max, y1_max) = box1
    (x2_min, y2_min), (x2_max, y2_max) = box2

    # Check if box1 is to the left of box2 or box2 is to the left of box1
    if x1_max < x2_min or x2_max < x1_min:
        return False

    # Check if box1 is above box2 or box2 is above box1
    if y1_max < y2_min or y2_max < y1_min:
        return False

    # If none of the above, the boxes intersect
    return True


detections = []

for idx, image_file in enumerate(image_files):
    image_path = os.path.join(evidence_folder, image_file)
    with open(image_path, 'rb') as f:
        image_data = f.read()

    response_data = detected_objects_info[idx]

    # Processing the image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 60)  # Adjust size as needed

    bad_color = "red"
    good_color= "green"
    confidence_threshold = 0.5

    detected_objects = response_data["customModelResult"]["objectsResult"]["values"]
    filtered_objects = [
        detected_object
        for detected_object in detected_objects
        if detected_object["tags"][0]["confidence"] >= confidence_threshold
    ]

    for detected_object in filtered_objects:
        tags = detected_object["tags"]
        description = " ".join((f"{tag['name']}: {tag['confidence']:.2f}" for tag in tags))
        coords = detected_object["boundingBox"]
        bounding_box = (
            (coords["x"], coords["y"]),
            (coords["x"] + coords["w"], coords["y"] + coords["h"]),
        )

        draw.rectangle(table_bounding_box, outline='blue', width=4)
        intersects = bounding_boxes_intersect(bounding_box, table_bounding_box)
        if intersects:
            print(f"{description} detected on table.")
            detections.extend([tag['name'] for tag in tags])

        color = bad_color if intersects else good_color

        draw.text((coords["x"], coords["y"]), description, font=font, fill=color)
        draw.rectangle(bounding_box, outline=color, width=8)

    # Display the image on subplot
    axs[idx].imshow(image)
    axs[idx].axis('off')
    axs[idx].set_title(image_file)

from collections import Counter
print(Counter(detections))

plt.tight_layout()
plt.show()


