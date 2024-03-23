from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load image tags and metadata
with open('image_tags.json') as f:
    image_data = json.load(f)

@app.route('/', methods=['GET'])
def home():
    selected_tag = request.args.get('tag')
    if selected_tag:
        # Filter images by the selected tag
        filtered_images = [image for image in image_data if selected_tag in image['tags']]
    else:
        # If no tag is selected, show all images
        filtered_images = image_data

    # Extract unique tags for sidebar or dropdown
    tags = set(tag for image in image_data for tag in image['tags'])
    return render_template('index.html', images=filtered_images, tags=sorted(tags), selected_tag=selected_tag)

if __name__ == '__main__':
    app.run(debug=True)
