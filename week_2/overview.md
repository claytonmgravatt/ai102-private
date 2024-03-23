

| Learning Path(s)                    | Modules   |
|-------------------------------------|-----------|
| Get Start with Azure AI Services    | Modules 1-5 |
| Create computer vision solutions with Azure AI vision | Module 1 |

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

### Creation and Consumption

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