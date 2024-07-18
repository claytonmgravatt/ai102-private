| Week | Date         | Learning Path                                                                                                                                                                               | Modules                         |
|------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|
| 10   | July 18, 2024 | [Develop Solutions with Azure AI Document Intelligence](https://learn.microsoft.com/en-us/training/paths/extract-data-from-forms-document-intelligence/)                                    | Modules 1-5                      |


## Study Guide Sections Covered

* Implement an Azure AI Document Intelligence solution
    - Provision a Document Intelligence resource
    - Use prebuilt models to extract data from documents
    - Implement a custom document intelligence model
    - Train, test, and publish a custom document intelligence model
    - Create a composed document intelligence model
    - Implement a document intelligence model as a custom Azure AI Search skill

# Develop Solutions with Azure AI Document Intelligence

### Resources Used

Document Intelligence

## Capabilities

### Supported File Types

| Model                  | PDF | Image: JPEG/JPG, PNG, BMP, TIFF, HEIF | Microsoft Office: Word (DOCX), Excel (XLSX), PowerPoint (PPTX), and HTML |
|------------------------|-----|---------------------------------------|------------------------------------------------------------------------|
| Read                   | ✔   | ✔                                     | ✔                                                                      |
| Layout                 | ✔   | ✔                                     | ✔ (2024-02-29-preview, 2023-10-31-preview)                             |
| General Document       | ✔   | ✔                                     |                                                                        |
| Prebuilt               | ✔   | ✔                                     |                                                                        |
| Custom extraction      | ✔   | ✔                                     |                                                                        |
| Custom classification  | ✔   | ✔                                     | ✔ (2024-02-29-preview)                                                 |


## [DEMO](https://documentintelligence.ai.azure.com/studio)

### Read
* Extract printed/handwritten text and position from documents.

```json
{
...  
"paragraphs": [
			{
				"spans": [
					{
						"offset": 0,
						"length": 188
					}
				],
				"boundingRegions": [
					{
						"pageNumber": 1,
						"polygon": [
							129,
							26,
							414,
							26,
							414,
							68,
							129,
							68
						]
					}
				],
				"content": "While healthcare is still in the early stages of its Al journey, we are seeing pharmaceutical and other life sciences organizations making major investments in Al and related technologies."
			},
...
}
```

### Layout
* Extract tables, checkboxes, titles, sectionheadings, and postion from documents.
```json
{
    ...
	"tables": [
        "rowCount": 3,
        "columnCount": 3,
        "cells": [
            ...
        ]
        "caption": {
        "content": "Table 1: This is a dummy table",
        "boundingRegions": [
            {
                "pageNumber": 1,
                "polygon": [
                    1.509,
                    6.1541,
                    3.4812,
                    6.1541,
                    3.4812,
                    6.3069,
                    1.509,
                    6.3069
                ]
            }
        ],
    ...
}
```

### General Document
* Extra Key:Value pairs, text, tables, structure, and Named Entities.
```json
{
    ...
    "keyValuePairs": [
        {
            "key": {
            "content": "Full Name:",
            }
            "value": {
            "content": "Raymond\nAmy",
            }
        }
    ...
}
```

### Prebuilt Models:

* Contract
* Health insurance card
* ID document
* Invoice
* Receipt
* US 1040 Tax*
* US 1098 Tax*
* US 1099 Tax*
* US W2 Tax
* US Mortgage 1003 URLA
* US Mortgage 1008 Summary
* US Mortgage closing
* disclosure
* Marriage certificate
* Credit card
* Business card

### Custom Models
* Custom classifier
    * What type of document is this?

* Custom template
    * Consistent visual template, first name is always 1 inch from the top left, for example.
    * Takes ~5 examples, ish.

* Custom neural
    * Structured, Semistructured, Unstructured documents
    * Takes "a large collection" of examples.

* Custom composed
    * Combination of multiple custom models.
    * Basically, classify this document and then send it to the correct model.
    * Up to 100 different models can be combined in paid, 5 in free.
        * Models must be of the same type (composed vs template)


#### Training Constraints
    * For PDF and TIFF, up to 2,000 pages can be processed (with a free tier subscription, only the first two pages are processed).

    * The file size for analyzing documents is 500 MB for paid (S0) tier and 4 MB for free (F0) tier.

    * Image dimensions must be between 50 x 50 pixels and 10,000 px x 10,000 pixels.

    * If your PDFs are password-locked, you must remove the lock before submission.

    * The minimum height of the text to be extracted is 12 pixels for a 1024 x 768 pixel image. This dimension corresponds to about 8-point text at 150 dots per inch.

    * For custom model training, the maximum number of pages for training data is 500 for the custom template model and 50,000 for the custom neural model.

    * For custom extraction model training, the total size of training data is 50 MB for template model and 1G-MB for the neural model.

    * For custom classification model training, the total size of training data is 1GB with a maximum of 10,000 pages.

#### Training files:
    Labeling easiest through Azure Portal.
    * Documents
    *.ocr.json
    *.labels.json
    *.fields.json


