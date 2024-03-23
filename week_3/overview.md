
| Learning Path(s)                                         | Modules   |
|----------------------------------------------------------|-----------|
| Create computer vision solutions with Azure AI vision    | Modules 2-4 |

## Study Guide Sections Covered 
* Implement custom computer vision models by using Azure AI Vision
   - Choose between image classification and object detection models
   - Label images
   - Train a custom image model, including image classification and object detection
   - Evaluate custom vision model metrics
   - Publish a custom vision model
   - Consume a custom vision model

* Analyze images
   - Convert handwritten text using Azure AI Vision

# Create computer vision solutions with Azure AI vision
Computer Vision Resource (demo?)
COCO labelling tool (Azure ML Studio)

## Custom Vision 

### Vocabulary
 - *Image Classification* - Image belongs to a class (or classes)..
    - This picture is of a cat.
    - This picture is of a [dog, animal]
    
 - *Object Detection* - A specific object in a specific location in the image.
    - Apple at coordinates x,y

## Face
 * Limited Access Policy 
   - Probably not on the exam

 * High risk

* Wall of Text
   - Face detection - for each detected face, the results include an ID that identifies the face and the bounding box coordinates indicating its location in the image.
   - Face attribute analysis - you can return a wide range of facial attributes, including:
      - Head pose (pitch, roll, and yaw orientation in 3D space)
      - Glasses (NoGlasses, ReadingGlasses, Sunglasses, or Swimming Goggles)
      - Blur (low, medium, or high)
      - Exposure (underExposure, goodExposure, or overExposure)
      - Noise (visual noise in the image)
      - Occlusion (objects obscuring the face)
      - Accessories (glasses, headwear, mask)
      - QualityForRecognition (low, medium, or high)
   - Facial landmark location - coordinates for key landmarks in relation to facial features (for example, eye corners, pupils, tip of nose, and so on)
   - Face comparison - you can compare faces across multiple images for similarity (to find individuals with similar facial features) and verification (to determine that a face in one image is the same person as a face in another image)
   - Facial recognition - you can train a model with a collection of faces belonging to specific individuals, and use the model to identify those people in new images.
   - Facial liveness - liveness can be used to determine if the input video is a real stream or a fake to prevent bad intentioned individuals from spoofing the recognition system.

## Read API
TODO: read handwritten text

