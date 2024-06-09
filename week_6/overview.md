| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 6    | June 13, 2024 | [Develop Natural Language Processing Solutions with Azure AI Services](https://learn.microsoft.com/en-us/training/paths/develop-language-solutions-azure-ai/)                                | Module 3                        |

## Study Guide Sections Covered

* Implement and manage a language understanding model by using Azure AI Language
    - Create intents and add utterances
    - Create entities
    - Train, evaluate, deploy, and test a language understanding model
    - Optimize a language understanding model
    - Consume a language model from a client application
    - Backup and recover language understanding models

# Develop natural language processing solutions with Azure AI Services

* Language Resource (demo?)

## Conversational Language Understanding

### Vocabulary

- Natural Language Processing (NLP) - Software interacting with "natural" (normal conversational) language
- Natural Language Understanding (NLU) - Subset of NLP focused on semantic meaning
- Conversational Language Understanding - Azure's custom NLU service
    - Utterances - Phrases or sentences people say
        * "Turn on the light", "Turn the fan on", "Switch on the light"
    - Intent - Task or action to perform
        * TurnOnDevice
    - Entities - Things that action might apply to
        * light, fan
        - Learned entities - New custom things you teach it
        - List entities - Enum (think, days of the week)
        - Prebuilt - Builtin list, things like numbers
        - Regex - Pattern based, regular expressions (think emails)

### Model Evaluation - _We'll do more with this next week..._
- Accuracy - Correct / Total
    - misleading in imbalanced samples
- Precision
    - Of those predicted as positive, how many are actually positive?
- Recall
    - Of those that are actually positive, how many were caught?
- F1 Score
    - Harmonic mean of Recall and Precision
        * Greater penalty to losers, 1.0 and 0.5 averages to 0.667 instead of 0.75.

## DEMO TIME!

## Example questions


### 1. Optimizing Intent Recognition:

In Azure Conversational Language Understanding, how can you improve the accuracy of intent recognition in scenarios where similar phrases might mean different things based on context?
- a. Increase the number of utterances per intent.
- b. Use a single intent for all phrases.
- c. Decrease the number of entities.
- d. All of the above.

### 2. Use of Entities in Language Understanding:

Which type of entity should you use in Azure Language Understanding to identify and extract a product name from user queries in a retail chatbot?
- a. Regular Expression entity
- b. Learned entity component
- c. Prebuilt domain entity
- d. List entity

### 3. Leveraging SDK:

Complete the following code:

```python
result = client.analyze_conversation(
    task={
        "kind": _________, # <---- Fill in the blank
        "analysisInput": {
            "conversationItem": {
                "participantId": "1",
                "id": "1",
                "modality": "text",
                "language": "en",
                "text": query
            },
            "isLoggingEnabled": False
        },
        "parameters": {
            "projectName": cls_project,
            "deploymentName": deployment_slot,
            "verbose": True
        }
    }
)
```

- a. "Conversation"
- b. "LanguageDetection"
- c. "Understanding"
- d. "ConversationSummary"

## Project idea: Bank assistant.