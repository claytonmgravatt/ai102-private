import os
import tkinter as tk
from tkinter import scrolledtext
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Load Azure credentials from environment variables
load_dotenv(override=True)
endpoint = os.environ.get("AZURE_LANGUAGE_ENDPOINT")
api_key = os.environ.get("AZURE_LANGUAGE_API_KEY")
credential = AzureKeyCredential(api_key)

# Create a Text Analytics client
text_analytics_client = TextAnalyticsClient(endpoint, credential)

# Named entity recognition settings
named_entity_recognition_project = "ai-102-demo-ner-med-proj"
named_entity_recognition_deployment = "med-prod"

def extract_entities():
    # Get the text from the text box
    note = text_box.get("1.0", tk.END)
    
    # Call Azure's text analytics service
    poller = text_analytics_client.begin_recognize_custom_entities(
        documents=[note.strip()],
        project_name=named_entity_recognition_project,
        deployment_name=named_entity_recognition_deployment,
    )
    
    # Wait for the service to process the request
    ner_results = list(poller.result())[0]
    
    # Clear previous results
    results_display.delete('1.0', tk.END)
    
    # Display the new results
    for entity in ner_results.entities:
        category, text = entity.category, entity.text
        results_display.insert(tk.END, f"{category}: {text}\n")

# Set up the main window
root = tk.Tk()
root.title("Medical Note Entity Extractor")

# Text input box
text_box = scrolledtext.ScrolledText(root, height=10, width=50)
text_box.pack(padx=10, pady=10)

# Button to extract entities
extract_button = tk.Button(root, text="Extract Entities", command=extract_entities)
extract_button.pack(pady=10)

# Text widget to display results
results_display = scrolledtext.ScrolledText(root, height=10, width=50)
results_display.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()


## Test text
# "Patient reports persistent sore throat and difficulty swallowing for over a week. Prescribed Penicillin for suspected streptococcal infection. Throat swab culture sent for lab analysis"