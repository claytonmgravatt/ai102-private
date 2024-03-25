| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 3    | May 16, 2024 | [Create computer vision solutions with Azure AI vision](https://learn.microsoft.com/en-us/training/paths/create-computer-vision-solutions-azure-ai/)                                        | Modules 2-4                     |

## Study Guide Sections Covered 
* Analyze images
   - Convert handwritten text using Azure AI Vision

* Implement custom computer vision models by using Azure AI Vision
   - Choose between image classification and object detection models
   - Label images
   - Train a custom image model, including image classification and object detection
   - Evaluate custom vision model metrics
   - Publish a custom vision model
   - Consume a custom vision model

# Create computer vision solutions with Azure AI vision

### Resources Used
Computer Vision Resource (demo?)

COCO image labelling tool (Azure ML Studio)

Azure Storage Account

## Read API
Two options for reading text:

- **Image Analysis:**
  - Ideal for unstructured documents or images with a small amount of text.
  - Provides immediate, synchronous results from a single API call.
  - Capabilities include text extraction, object detection, and image categorization.
  - Examples: street signs, handwritten notes, store signs.
```python
image_analysis = image_analysis_client.analyze(
    image_data=image_data, visual_features=[VisualFeatures.READ]
)
```

- **Document Intelligence:** <-- We'll cover this later!
  - Suitable for reading text from small to large volumes in images and PDF documents.
  - Utilizes document context and structure to enhance accuracy.
  - Operates asynchronously, requiring an operation ID for result retrieval.
  - Examples: receipts, articles, invoices.

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

## Custom Vision 

### Vocabulary
 - *Image Classification* - Image belongs to a class (or classes)..
    - This picture is of a cat.
    - This picture is of a [dog, animal]
    
 - *Object Detection* - A specific object in a specific location in the image.
    - Apple at coordinates x,y

---

## Example Questions

### 1. Reading Receipts
You're helping a small business automate reading receipts. What service should you use?

- A. Image Analysis
- B. Text Analysis
- C. Object Detection
- D. Document Intelligence

### 2.  OCR Sizing
When using the Read OCR function, how are the results structured for easier text extraction and analysis?

- A. The results are returned asynchronously as a binary stream, divided into pages and paragraphs.
- B. The results are returned synchronously, organized hierarchically into blocks, lines, and words, with text values provided at both the line and word levels.
- C. The results are only provided at the word level.
- D. The results are encoded in an image format, with metadata describing text location and font size.

### 3. Location

You need to determine when cats are on the counter within an image. You should use Custom Image Classification.

A. True  
B. False