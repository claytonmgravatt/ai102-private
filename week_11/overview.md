| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 11   | July 25, 2024| [Develop Generative AI solutions with Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/)                                            | Modules 1-7                     |


## Study Guide Sections Covered
### Implement generative AI solutions (10–15%)
* Use Azure OpenAI Service to generate content
    - Provision an Azure OpenAI Service resource
    - Select and deploy an Azure OpenAI model
    - Submit prompts to generate natural language
    - Submit prompts to generate code
    - Use the DALL-E model to generate images
    - Use Azure OpenAI APIs to submit prompts and receive responses

* Optimize generative AI
    - Configure parameters to control generative behavior
    - Apply prompt engineering techniques to improve responses
    - Use your own data with an Azure OpenAI model
    - Fine-tune an Azure OpenAI model

### Resources Used

Azure OpenAI

### Capabilities

Generative Text Models (GPT-35-Turbo, GPT4, GPT4o)
Geneartive Image Models (DALL-E 2, DALL-e 3)
Embeddings Models (tet-embedding-ada-002, text-embedding-3-large)

## Chat Models

### Playground
https://oai.azure.com/portal/chat

#### Parameters
Temperature - Higher is more random.
Top P - Higher is more random.
Max Response - Maximum number of tokens to respond with.

### Endpoints
Completion:
    - Input prompt -> text completion. 
    "Finish this sentence: The chicken cross the"

ChatCompletion: (the only one you should care about, what modern models use)
    - Input chat conversation -> Next message completion.

```json
    {"role": "system", "content": "You are a helpful assistant, teaching people about AI."},
    {"role": "user", "content": "Does Azure OpenAI support multiple languages?"},
    {"role": "assistant", "content": "Yes, Azure OpenAI supports several languages, and can translate between them."},
    {"role": "user", "content": "Do other Azure AI Services support translation too?"}
```

### Prompting Hints

* Provide clear instructions, being descriptive as possible.

* Plan for recency bias, where the model pays more attention to what was said at the end.

* Use clear section markers like "---"

* Use grounding content when appropriate.

* Use cues, especially for code generation. _Ending your sql request prompt with SELECT_

* Misc: Chain of Thought, Cite Your Sources, "You are smart", few-shot

### Fine Tuning
* Provide examples of desired outputs
* Host a retrained version of the model _Hosting $1.70 per hour, training ~$0.008 per 1000 tokens._

### Assistants API
* Instructions
* Tools (128 per assistant)
    * Code Interpreter - _Write and run code in a sandboxed execution environment, $0.03/session_
    * File Search - _Upload, then automatically chunk and embed documents for retrieval. Up to 10,000 files per assistant, not currently billed but probably $6/GB/Month, charged daily._
    * Functions - _Custom function definitions to be called._

## Image Models


* Supports various sizes

    - 1792 * 1024

    - 1024 * 1024

DALLE 2
![DALLE2 Painting](<dalle/A painting of a pastoral landscape in the style of rembrandt.png>)

DALLE 3
![DallE3 Painting](<dalle/A painting of a pastoral landscape in the style of rembrandt (1).png>)
