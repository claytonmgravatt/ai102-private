| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 4    | May 23, 2024 | [Create computer vision solutions with Azure AI vision](https://learn.microsoft.com/en-us/training/paths/create-computer-vision-solutions-azure-ai/) <br> [Develop Decision Support Solutions with Azure AI Services](https://learn.microsoft.com/en-us/training/paths/develop-decision-support/) | Module 5 (+ spatial analysis) <br> Module 1 |

## Study Guide Sections Covered 

* Analyze videos
    - Use Azure AI Video Indexer to extract insights from a video or live stream
    - Use Azure AI Vision Spatial Analysis to detect presence and movement of people in video

* Create solutions for content delivery
    - Implement a text moderation solution with Azure AI Content Safety
    - Implement an image moderation solution with Azure AI Content Safety


# Create computer vision solutions with Azure AI vision

* Azure AI Video Indexer
* Azure AI Vision


## Video Indexer 

Used to extract information from videos.

* Facial recognition - detecting the presence of individual people in the image.
* Optical character recognition - reading text in the video.
* Speech transcription - creating a text transcript of spoken dialog in the video.
* Topics - identification of key topics discussed in the video.
* Sentiment - analysis of how positive or negative segments within the video are.
* Labels - label tags that identify key objects or themes throughout the video.
* Content moderation - detection of adult or violent themes in the video.
* Scene segmentation - a breakdown of the video into its constituent scenes.

* Supports custom speech models
* Supports custom brand/product recognition

###  Demo time!


## Spatial Analysis

* Counting people in area
* Monitor social distancing
* Detect when people cross a line

* Video Summary / Retrieval
    "find frame with person in pink jacket"

### Demo time, part 2!

# Develop Decision Support Solutions with Azure AI Services

* Content Safety resource
* Content Moderator resource

## Content Moderator for Text / Images
! Deprecated ! - but it might still be on the test

* Profanity
* Classification
    - Category 1: Sexually explicit or adult
    - Category 2: Sexually suggestive or mature
    - Category 3: Offensive
* Personal data

## Content Safety for Text / Images
The cool, new and improved one.

* Harm detection categories
    - Hate and Fairness (things like hate speech)
    - Sexual (things like the Outlander novels)
    - Violence (weapons, intentions to do harm)
    - Self-harm (harming one's self)

* Severity Levels (0-7)

* Other stuff too
    - Prompt shield : Protection from prompt injection
    - Groundedness detection : Protection(ish) from hallucinations

### Demo time, part 3!

## Example Questions

### 1. Post moderation

You have a blog website that allows users to comment. You're using Azure AI Content Safety's text analysis feature to detect harmful content. Which of the following should you review?

- A. `{'categoriesAnalysis': [{'category': 'Hate', 'severity': 4}]}`
- B. `{'categoriesAnalysis': [{'category': 'Hate', 'severity': 0}]}`


### 2. Stay off the tracks

You're managing a subway station and want to monitor a live camera video feed for when someone inadvertently falls onto the tracks. Which Azure resource should you utilize?

- A. Azure AI Custom Vision
- B. Azure AI Video Indexer
- C. Azure AI Vision Spatial Analysis
- D. Azure AI Content Safety


### 3. Obtuse jargon

Your company uses fancy made up words like API, Monads, and Nullability, which aren't getting properly identified in your AI indexed videos. What should you do?

- A. Add C# to the list of automatically detected languages.
- B. Upload a plain-text dataset of industry-specific words to Azure AI Video Indexer's model customizations section.
- C. Train a seperate custom speech model, transcribe the videos, and upload a transcript. 
- D. Give up.

## Project idea: Slick video indexing website.