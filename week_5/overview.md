
| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 5    | June 6, 2024 | [Develop Natural Language Processing Solutions with Azure AI Services](https://learn.microsoft.com/en-us/training/paths/develop-language-solutions-azure-ai/)                                | Module 2                        |


## Study Guide Sections Covered
* Create a question answering solution by using Azure AI Language
    - Create a question answering project
    - Add question-and-answer pairs manually
    - Import sources
    - Train and test a knowledge base
    - Publish a knowledge base
    - Create a multi-turn conversation
    - Add alternate phrasing
    - Add chit-chat to a knowledge base
    - Export a knowledge base
    - Create a multi-language question answering solution

## Develop Natural Language Processing Solutions with Azure AI Services
* Language Resource
    * Azure AI Search Resource (we'll learn about this later)

## Custom Question Answering

* Knowledge base - set of question and answer pairs
    - FAQs - Can create from URL
    - Unstructured Text
    - "Chit Chat" - built in conversational pleasantries
### _Discuss: Does Chit Chat help or hinder?_

* Multi-language support
    - Project per language
        - OR
    - Translatation Service: Translate Question -> Fetch Answer -> Translate Answer

* Multi-turn conversations
    - "Follow up prompts"
    - Follow up promps can be restricted to only show after parent, or searchable

* Alternate Questions / Synonyms

* Filterable metadata tags
    - filter answer to be relevant to specific region, for example

* Exportable/Importable to Excel/TSV

* Testable before deployment

* Automated Suggestions - Active Learning

* One(ish) click deployment

## Comparison to modern R.A.G.
* More consistent answers
* More control over answers
* Less flexible
    * Only really for static information
    * Limited to what it can parse + what's manually entered
### _Discuss: What is RAG, why ever use this instead?_

## Example Questions

### 1. Novelty

You are developing a solution to provide instant customer support using the Azure Custom Question Answering. You want to ensure the system can handle queries it has not been trained on by providing a default response. Which of the following actions should you take?
- a. Increase the minimum score threshold for answers.
- b. Decrease the confidence score threshold.
- c. Implement a fallback mechanism in your application logic.
- d. Train the model with a broader dataset.

### 2. Up to date information

Azure Custom Question Answering automatically updates its knowledge base with new information from the internet.
- a. True
- b. False

### 3. Improving performance

Question: You are tasked with improving the accuracy of a Custom Question Answering model used for technical support in your organization. During the review, you notice that certain technical terms are often misunderstood by the model. What is the most effective strategy to improve the model's understanding of these terms?
- a. Reducing the number of terms in each query to simplify the questions.
- b. Incorporating more documents containing these technical terms into the knowledge base.
- c. Switching to a different Azure cognitive service that handles technical queries.
- d. Manually programming responses for queries containing these terms.

## Project idea: Helpful QnA bot on product page.