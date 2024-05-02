| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 1    | May 2, 2024  | [Develop Natural Language Processing Solutions with Azure AI Services](https://learn.microsoft.com/en-us/training/paths/develop-language-solutions-azure-ai/)                               | Module 1                        |
## Study Guide Sections Covered 
* Analyze text by using Azure AI Language
    - Extract key phrases

    - Extract entities

    - Determine sentiment of text

    - Detect the language used in text

    - Detect personally identifiable information (PII) in text


# Develop natural language processing solutions with Azure AI Services

* Language Resource (demo?)


## Text Analytics


* Language detection - determining the language in which text is written.

* Key phrase extraction - identifying important words and phrases in the text that indicate the main points.

* Sentiment analysis - quantifying how positive or negative the text is.

* Named entity recognition - detecting references to entities, including people, locations, time periods, organizations, and more.

* Entity linking - identifying specific entities by providing reference links to Wikipedia articles.

### DEMO!

## Example Questions

### 1. Email Routing by Language
You need to ensure user emails are routed to the correct language-speaking department. Which method would you use?

```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

endpoint = os.environ.get("AZURE_LANGUAGE_ENDPOINT")
api_key = os.environ.get("AZURE_LANGUAGE_API_KEY")
credential = AzureKeyCredential(api_key)

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
result = text_analytics_client.________(documents=[example_text]) # Fill in the blank.
```
Options:
- a. `detect_language`
- b. `extract_key_phrases`
- c. `recognize_language`
- d. `recognize_key_phrases`

### 2. Sentiment Analysis for Product Reviews
You are using sentiment analysis to categorize product reviews. Based on the sentiment scores below, what is the overall sentiment of this review?

```json
{'positive': 0.04, 'neutral': 0.25, 'negative': 0.71}
```


## Project idea: Message board opinion mining.