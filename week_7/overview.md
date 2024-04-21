| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 7    | June 13, 2024| [Develop Natural Language Processing Solutions with Azure AI Services](https://learn.microsoft.com/en-us/training/paths/develop-language-solutions-azure-ai/)                                | Modules 4-5                     |

## Study Guide Sections Covered

* Analyze text by using Azure AI Language
    - Extract entities

_Also overlaps with CLU concepts._

# Develop natural language processing solutions with Azure AI Services

### Resources Used

Language

## Custom Text Classification

* Similar to "Intent" from Conversational Language Understanding
* Types of projects:
    - **Single Label** : Everything falls into only 1, mutually exclusive bucket
        - ex. "Cat vs. Dog" animal classification.
    - **Multiple label** : Things can fall into multiple, overlapping categories.
        - ex. "Action and Adventure" movie genres.
* Model predictions:
    - **True positive**: model predicts _x_ and entity is _x_.
        - ex. Someone with covid tested positive for covid.
    - **True negative**: models predicts _not x_ and entity is _not x_.
        - ex. Someone without covid tested negative for covid.
    - **False positive**: model predicts _x_ but entity is _not x_.
        - ex. Someone without covid tested positive for covid.
    - **False negative**: model predicts _not x_ but entity is _x_.
### _Dicuss: Which is worse, a False Negative or a False Positive?_
* Model evaluation:
    - **Recall** : Of all actual _x_, how many did the model catch?
    - **Precision**: Of things model said was x, how many were actually x?
    - **F1 Score**: Harmonic mean of Recall and Precision, penalizing larger discrepancies.
        -ex. average of 0.5 recall and 1.0 Precision would be 0.67, instead of 0.75. 
    - **Accuracy**: Correct predictions / total predictions.
### _Discuss: 99% accurate model for disease affecting 1% of population._
* Training vs testing datasets:
    - Some data is hidden from the model during training to use for later evaluation.
### _Discuss: Why hold out data?_        
* Model deployment:
    - Supports multiple model deployment slots.
* Set up [CORS](https://learn.microsoft.com/en-us/azure/ai-services/language-service/custom-text-classification/how-to/create-project?tabs=azure-portal%2Cstudio%2Cmulti-classification#enable-cors-for-your-storage-account) for linked storage account. 

### Demo time!

## Custom Named Entity Recognition

* Similar to "entities" from Conversational Language Understanding
* Data Labeling Guidelines
    - Consistency - Label all examples the same way
    - Precision: Label only the entities themselves (beware extra words)
    - Completeness: Label all instances of the entities (don't miss examples)
### _Discuss: What would you do if your model had high recall but low precision?_ 

* Can be labeled in Language studio or by providing standardized JSON


#Example, health care records? Extracting fields from notes, maybe classifying?

## Example questions

### 1. Herd health.
Your large herd of cattle is being affected by Perterbed Cow Disease and you want to train a machine learning model to help identify which few cows have the disease.
Which metric would be most important to consider if a disease affects a small percentage of the population and the cost of missing a case (false negative) is very high?
- a. Precision
- b. Accuracy
- c. Recall
- d. F1 Score

### 2. Data preparedness.
When preparing data for training a Custom Named Entity Recognition model in Azure, what is an essential step?
- a. Normalizing numerical data to prevent model bias.
- b. Annotating texts with the named entities to be recognized by the model.
- c. Encrypting data to ensure privacy before uploading to the cloud.
- d. Converting all text data to lowercase to simplify the model architecture.

### 3. Label residency.
You've just finished labeling your custom text classification data. To view the label file that will be used to view your model, you can nagivate to the CustomText.xml file in the linked storage account.
- a. True
- b. False

### 4. Tech choice.
Which of the following accurately describes the deciding factors for when to choose Custom Text Classification over Custom Named Entity Recognition?

- a. Use Custom Text Classification when you need to identify specific words or phrases within text data, and Custom NER when categorizing whole documents into predefined categories.
- b. Choose Custom Text Classification when categorizing whole documents or phrases into predefined categories, and Custom NER when the goal is to extract specific entities like names, dates, or locations from text.
- c. Opt for Custom Text Classification if you require real-time processing and scalability, while Custom NER should be used for batch processing of large datasets.
- d. Select Custom NER when the text data is unstructured and diverse, and Custom Text Classification when the data is homogeneous and structured.