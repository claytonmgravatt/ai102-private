

| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 2    | May 9, 2024  | [Get Started with Azure AI Services](https://learn.microsoft.com/en-us/training/paths/get-started-azure-ai/) <br> [Create computer vision solutions with Azure AI vision](https://learn.microsoft.com/en-us/training/paths/create-computer-vision-solutions-azure-ai/) | Modules 1-5 <br> Module 1       |

## Study Guide Sections Covered 
* Plan, create and deploy an Azure AI service
    - Plan for a solution that meets Responsible AI principles
    - Create an Azure AI resource
    - Determine a default endpoint for a service
    - Plan and implement a container deployment

* Manage, monitor, and secure an Azure AI service
    - Configure diagnostic logging
    - Monitor an Azure AI resource
    - Manage costs for Azure AI services
    - Manage account keys
    - Protect account keys by using Azure Key Vault
    - Manage authentication for an Azure AI Service resource
    - Manage private communications

* Analyze images
    - Select visual features to meet image processing requirements
    - Detect objects in images and generate image tags
    - Include image analysis features in an image processing request
    - Interpret image processing responses
    - Extract text from images using Azure AI Vision



# Get Start with Azure AI Services

### Vocabulary

- AI/ML
- Model training / Inferencing

### Ethical Considerations

- Implicit Bias (amazon)
- Self-fulfilling prophecies (policing/education)
- Accuracy vs fairness (99% vs 95%)


- **Fairness:** AI systems should ensure fair treatment across all demographics, actively working to eliminate bias from machine learning models through rigorous evaluation and mitigation strategies.
  
- **Reliability and Safety:** AI systems must achieve high reliability and safety, especially in critical applications like autonomous vehicles or healthcare diagnostics, through comprehensive testing and deployment management.
  
- **Privacy and Security:** AI systems need to secure data and respect user privacy, implementing safeguards to protect personal information throughout the system's lifecycle.
  
- **Inclusiveness:** AI should empower and engage everyone, being developed with input from diverse groups to ensure benefits are accessible across all sections of society.
  
- **Transparency:** AI systems should be transparent, making users aware of their purpose, workings, limitations, and how data is used and retained.
  
- **Accountability:** People behind AI systems are accountable for their design and operation, ensuring they meet ethical and legal standards within a governance framework.

### Creation and Consumption - Demo time!

- Push create button. Call consume API.

### Security

- The usual. 
- IP / RBAC / Entra ID 

### Monitoring

- Metrics / Alerts
- Diagnostic logging

### Containerization !important

Most services have images available.

```shell
docker run --rm -it -p 5000:5000 --memory 12g --cpus 1 mcr.microsoft.com/azure-cognitive-services/textanalytics/language:latest Eula=accept Billing=<yourEndpoint> ApiKey=<yourKey>
```

Required: 
```
Eula=accept
Billing=<yourEndpoint>
ApiKey=<yourKey>
```

# Create computer vision solutions with Azure AI vision

- "Computer Vision" resource (demo?)

## Image Analysis

 - *Description and tag generation* - determining an appropriate caption for an image, and identifying relevant "tags" that can be used as keywords to indicate its subject.
 - *Object detection* - detecting the presence and location of specific objects within the image.
 - *People detection* - detecting the presence, location, and features of people in the image.
- *Background removal* - detecting the background in an image and output the image with the background transparent or a greyscale alpha matte image.
- *Optical character recognition* - reading text in the image.
- *Smart thumbnail generation* - identifying the main region of interest in the image to create a smaller "thumbnail" version.

- *see notebook*


---

## Example Questions

### 1. Region Description in Images
You need to create a description for each region within an image. Which visual features should you extract? Fill in the blank with the correct visual feature:

```python
image_analysis = image_analysis_client.analyze(
    image_data=image_data, visual_features=[VisualFeatures.________] # Fill in the blank
)
```
**Options:**
- a. `DENSE_CAPTIONS`
- b. `SMART_CROPS`
- c. `CAPTION`
- d. `SMART_TAGS`

### 2. Extracting Foreground from Images
You need to extract the foreground from an image. Complete the URL in the space provided:

```python
api_version = "2023-02-01-preview"
mode="backgroundRemoval"
url = f"https://ai-102-demo-compvision-eus.cognitiveservices.azure.com/computervision/imageanalysis:_________?api-version={api_version}&mode={mode}" # Complete the URL
```
**Options:**
- a. segment
- b. backgroundRemoval
- c. foregroundMatting
- d. foregroundRecognizer

### 3. Responsible AI Principles
You are developing a new sales system that will process the video and text from a public-facing website.  
You plan to monitor the sales system to ensure that it provides equitable results regardless of the user's location or background.  
Which two responsible AI principles provide guidance to meet the monitoring requirements? Each correct answer presents part of the solution.  
**NOTE:** Each correct selection is worth one point.

- A. transparency
- B. fairness
- C. inclusiveness
- D. reliability and safety
- E. privacy and security
