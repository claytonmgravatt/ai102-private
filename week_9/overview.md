| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 9    | July 11, 2024| [Implement Knowledge Mining with Azure AI Search](https://learn.microsoft.com/en-us/training/paths/implement-knowledge-mining-azure-cognitive-search/)                                      | Modules 1-5                     |


## Study Guide Sections Covered

* Implement an Azure AI Search solution
    - Provision an Azure AI Search resource
    - Create data sources
    - Create an index
    - Define a skillset
    - Implement custom skills and include them in a skillset
    - Create and run an indexer
    - Query an index, including syntax, sorting, filtering, and wildcards
    - Manage Knowledge Store projections, including file, object, and table projections

# Implement Knowledge Mining with Azure AI Search

* AI Search Resource

### Vocabulary

#### Content Components
- Index 
    - Searchable collection of stuff (documents, data).
    - Has a defined set of fields
    - Like a table in a database.
- Indexer
    - Engine that can be used to pull data from external sources into an index.
    - One way to populate your tables (alteratively can push data)
- Skills
    - Functions an indexer can apply to help extract / enrich / transform data.
        - Other AI services we've already seen + some specific to Search.
- Skillset
    - Collections of skills an indexer uses.
        - _Crack open and extract text from Power Point files_
        - _Split text into chunks_
        - _Extract keywords from chunks_
        - _Generate embeddings for those chunks_

- Datasources
    - Where indexers pull data from

- Knowledge Stores
    - Optional additional data stores to persist data from indexers.

        
#### Management Components
- Replicas
    * Copied instances of the search service.
    * Helps with many concurrent requests.
- Partitions
    * Subdivide an index into multiple storage locations
    * Allows for more targeted querying/reindexing.
- Search units
    * Replicas x Partitions = Search Units. 


## DEMO TIME! (integrated vectorization)

## Searching an Index
### - Simple Search  (queryType=simple)
[Examples](https://learn.microsoft.com/en-us/azure/search/search-query-simple-examples)
```json
{
    "search": "budget hotel +pool",
    "filter": "Rating ge 2 and Rating lt 4",
    "select": "HotelId, HotelName, Rating",
    "orderby": "Rating desc",
    "count": true
}
```
### - Full (queryType=full)
Uses lucene syntax.
[Examples](https://learn.microsoft.com/en-us/azure/search/search-query-lucene-examples)

 - **Boolean Operators**
     - `AND`, `OR`, `NOT`
     - Example: `luxury AND 'air con'`
 
 - **Fielded Search**
     - `fieldName:search term`
     - Example: `Description:luxury AND Tags:air con`
 
 - **Fuzzy Search**
     - `~`
     - Example: `Description:luxury~` returns results with misspelled versions of luxury
 
 - **Term Proximity Search**
     - `"term1 term2"~n`
     - Example: `"indoor swimming pool"~3` returns documents with the words "indoor swimming pool" within three words of each other
 
 - **Regular Expression Search**
     - `/regular expression/`
     - Example: `/[mh]otel/` would return documents with hotel and motel
 
 - **Wildcard Search**
     - `*`, `?`
         - `*` matches many characters
         - `?` matches a single character
     - Example: `'air con'*` would find air con and air conditioning
 
 - **Precedence Grouping**
     - `(term AND (term OR term))`
     - Example: `(Description:luxury OR Category:luxury) AND Tags:air?con*`
 
 - **Term Boosting**
     - `^`
     - Example: `Description:luxury OR Category:luxury^3` would give hotels with the category luxury a higher score than luxury in the description
 

    - Wildcard search example:
```json
{
    "search": "HotelName:sc*",
    "queryType": "full",
    "select": "HotelName",
    "count": true
}
```
### - Semantic Reranker (queryType=semantic)
- Takes top 50 most relevant documents (based on BM25 ranking function), then passes results to a language understanding model that reorders the results. 
- Also extracts most relevant text and can provide answers to questions.
    - _ChatGPT, which of these documents is most relevant?_
```json
{
      "queryType": "semantic",
      "queryLanguage" : "en-us",
      "search": "all hotels near the water" , 
      "semanticConfiguration": "hotels-conf" , 
      "searchFields": "",
      "answers": "extractive|count-3",
      "count": true
}
```

### - Vector (can be combined with other query types)
- Finds similar results based on vector representations.
```json
    {
        "count": true,
        "select": "HotelId, HotelName, Description, Category",
        "vectorQueries": [
            {
                "vector": [0.01944167, 0.0040178085
                    . . .  TRIMMED FOR BREVITY
                    010858015, -0.017496133],
                "k": 7,
                "fields": "DescriptionVector",
                "kind": "vector",
                "exhaustive": true
            }
        ]
    }
```


### - Hybrid (vector + some other keyword based search type)
```json
{
    "count": true,
    "search": "historic hotel walk to restaurants and shopping",
    "select": "HotelId, HotelName, Category, Description,Address/City, Address/StateProvince",
    "filter": "geo.distance(Location, geography'POINT(-77.03241 38.90166)') le 500",
    "vectorFilterMode": null,
    "facets": [ "Address/StateProvince"],
    "top": 7,
    "queryType": "semantic",
    "answers": "extractive|count-3",
    "captions": "extractive|highlight-true",
    "semanticConfiguration": "my-semantic-config",
    "vectorQueries": [
        {
            "vector": [ 0.01944167, 0.0040178085, .... ],
            "k": 7,
            "fields": "DescriptionVector",
            "kind": "vector",
            "exhaustive": true
        }
    ]
}
```

### Other ways to improve search results
- Synonym maps
    * UK = United Kingdom
- Scoring profiles
    * Used to weight the importance of fields when searching.
        - _Description is 5 times as important as the name_
- Analyzers 
    * Used to preprocess text
        - _Strip HTML, remove stopwords like "the", reduce "jumps" to "jump"_
    * Can define custom analyzers.

## Skills
- Many exist out the box, but if you want "custom" ones you can define an http endpoint to catch, transform, and return data.

### Custom Skills

Input Schema
```json
{
    "values": [
      {
        "recordId": "<unique_identifier>",
        "data":
           {
             "<input1_name>":  "<input1_value>",
             "<input2_name>": "<input2_value>",
             ...
           }
      },
      {
        "recordId": "<unique_identifier>",
        "data":
           {
             "<input1_name>":  "<input1_value>",
             "<input2_name>": "<input2_value>",
             ...
           }
      },
      ...
    ]
}
```
Output Schema
```json
{
    "values": [
      {
        "recordId": "<unique_identifier_from_input>",
        "data":
           {
             "<output1_name>":  "<output1_value>",
              ...
           },
         "errors": [...],
         "warnings": [...]
      },
      {
        "recordId": "< unique_identifier_from_input>",
        "data":
           {
             "<output1_name>":  "<output1_value>",
              ...
           },
         "errors": [...],
         "warnings": [...]
      },
      ...
    ]
}
```
Add to skillset
```json
{
    "skills": [
      ...,
      {
        "@odata.type": "#Microsoft.Skills.Custom.WebApiSkill",
        "description": "<custom skill description>",
        "uri": "https://<web_api_endpoint>?<params>",
        "httpHeaders": {
            "<header_name>": "<header_value>"
        },
        "context": "/document/<where_to_apply_skill>",
        "inputs": [
          {
            "name": "<input1_name>",
            "source": "/document/<path_to_input_field>"
          }
        ],
        "outputs": [
          {
            "name": "<output1_name>",
            "targetName": "<optional_field_name>"
          }
        ]
      }
  ]
}
```

- Example Chunk/Embed Skillset
```json
{

  "skills": [
    {
      "@odata.type": "#Microsoft.Skills.Text.SplitSkill",
      "name": "#1",
      "description": "Split skill to chunk documents",
      "context": "/document",
      "defaultLanguageCode": "en",
      "textSplitMode": "pages",
      "maximumPageLength": 2000,
      "pageOverlapLength": 500,
      "maximumPagesToTake": 0,
      "inputs": [
        {
          "name": "text",
          "source": "/document/content"
        }
      ],
      "outputs": [
        {
          "name": "textItems",
          "targetName": "pages"
        }
      ]
    },
    {
      "@odata.type": "#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill",
      "name": "#2",
      "description": null,
      "context": "/document/pages/*",
      "resourceUri": "https://ai-102-demo-openai-eus.openai.azure.com",
      "apiKey": "<redacted>",
      "deploymentId": "ai-102-demo-embedding-3-large",
      "dimensions": 3072,
      "modelName": "text-embedding-3-large",
      "inputs": [
        {
          "name": "text",
          "source": "/document/pages/*"
        }
      ],
      "outputs": [
        {
          "name": "embedding",
          "targetName": "text_vector"
        }
      ],
      "authIdentity": null
    }
  ]
}
```

## Knowledge Store Projections
 - You may want to save your enriched and extracted data elsewhere.
```json
"knowledgeStore": { 
      "storageConnectionString": "<storage_connection_string>", 
      "projections": [
        {
            "objects": [
                {
                "storageContainer": "<container>",
                "source": "/projection"
                }
            ],
            "tables": [],
            "files": []
        },
        {
            "objects": [],
            "tables": [
                {
                "tableName": "KeyPhrases",
                "generatedKeyName": "keyphrase_id",
                "source": "projection/key_phrases/*",
                },
                {
                "tableName": "docs",
                "generatedKeyName": "document_id", 
                "source": "/projection" 
                }
            ],
            "files": []
        },
        {
            "objects": [],
            "tables": [],
            "files": [
                {
                "storageContainer": "<container>",
                "source": "/document/normalized_images/*"
                }
            ]
        }
    ]
 }
 ```

## Field types

- **key**: Fields that define a unique key for index records.
- **searchable**: Fields that can be queried using full-text search.
- **filterable**: Fields that can be included in filter expressions to return only documents that match specified constraints.
- **sortable**: Fields that can be used to order the results.
- **facetable**: Fields that can be used to determine values for facets (user interface elements used to filter the results based on a list of known field values).
- **retrievable**: Fields that can be included in search results (by default, all fields are retrievable unless this attribute is explicitly removed).


## Questions

### Question 1:
**You are implementing an Azure AI Search solution to index data from various external sources. You need to ensure that the data is automatically pulled into the index and enriched using AI skills. Which component should you configure for this task?**

A) Index

B) Indexer

C) Replica

D) Knowledge Store

<details>
  <summary>Click to reveal</summary>
**Answer: B) Indexer**
</details>


### Question 2:
**You have created an Azure AI Search index for a hotel booking website. You want to perform a full-text search that returns hotels with a rating between 2 and 4, sorted by rating in descending order. Fill in the blank to complete the search query:**

```json
{
    "search": "budget hotel +pool",
    "filter": "Rating ge 2 and Rating lt 4",
    "select": "HotelId, HotelName, Rating",
    "orderby": "Rating desc",
    "count": true
}
```

**In this scenario, the `filter` expression correctly limits the search results to hotels with ratings between 2 and 4. Which field attribute ensures that the `Rating` field can be used in the `filter` expression?**

A) searchable

B) filterable

C) sortable

D) retrievable

<details>
  <summary>Click to reveal</summary>
**Answer: B) filterable**
</details>


### Question 3:
**You are configuring a search query in Azure AI Search to return a list of hotels with specific criteria. You want to perform a full-text search using the Lucene syntax to find hotels that either have the keyword 'luxury' in the description or belong to the 'luxury' category, with a higher relevance for the category match. Fill in the blanks in the search query:**

```json
{
    "search": "(Description:luxury OR Category:luxury^3)",
    "queryType": "____",
    "select": "HotelId, HotelName, Description, Category",
    "count": true
}
```

**What should be used to fill in the blank for `queryType` to achieve the desired functionality?**

A) simple

B) full

C) semantic

D) vector




<details>
  <summary>Click to reveal</summary>
**Answer: B) full**
</details>


## Project idea: Docs information retrieval.
[Link](https://portal.azure.com/#@IntelliTect.com/resource/subscriptions/b22b399d-3ab9-402c-b507-7f710e797b06/resourceGroups/ai-102-demo-rg/providers/Microsoft.Search/searchServices/ai-102-demo-search-eus/indexers)