import os
import json
import requests

from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from wordcloud import WordCloud
import matplotlib.pyplot as plt

load_dotenv(override=True)
endpoint = os.environ.get("AZURE_LANGUAGE_ENDPOINT")
api_key = os.environ.get("AZURE_LANGUAGE_API_KEY")
credential = AzureKeyCredential(api_key)

text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

sentiment_pairs_path = 'sentiment_key_phrases.json'
yammer_data_path = 'yammer_data.json'
yammer_access_token='123'

def fetch_all_messages(yammer_access_token):
    base_url = 'https://www.yammer.com/api/v1/messages.json'
    headers = {'Authorization': f'Bearer {yammer_access_token}'}
    
    all_messages = []
    older_than = None  # Start with no older_than to fetch the most recent messages

    for _ in range(10):
        print(f'Starting {older_than} offset...')
        if older_than:
            # Append older_than to the URL if it's specified
            url = f'{base_url}?older_than={older_than}'
        else:
            url = base_url
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error fetching messages: {response.status_code}")
            break
        
        data = response.json()
        messages = data.get('messages', [])
        
        if not messages:
            break  # No more messages to fetch
        
        # Update older_than with the ID of the last message fetched
        older_than = messages[-1]['id']

        for message in messages:
            group_id = message.get('group_id', '')
            parsed_text = message.get('body', {'parsed':''}).get('parsed', '')
            if len(parsed_text) > 0:
                redacted_text = text_analytics_client.recognize_pii_entities(documents=[parsed_text])[0].redacted_text
                all_messages.append({'group_id':group_id, 'redacted_text':redacted_text})

    return all_messages

def process_documents_in_batches(documents):
    results = []

    # Process documents in batches of 10
    for i in range(0, len(documents), 10):
        batch = documents[i:i+10]
        texts = [message['redacted_text'] for message in batch]

        # Extract key phrases
        key_phrases_result = text_analytics_client.extract_key_phrases(documents=texts)
        key_phrases = [result.key_phrases for result in key_phrases_result]

        # Analyze sentiment
        sentiment_result = text_analytics_client.analyze_sentiment(documents=texts)
        sentiments = [result.sentiment for result in sentiment_result]

        # Combine results
        batch_results = [{'sentiment': sentiment, 'key_phrases': phrases}
                         for sentiment, phrases in zip(sentiments, key_phrases)]
        results.extend(batch_results)

    return results    

if not os.path.exists(yammer_data_path):
    messages = fetch_all_messages(yammer_access_token)
    output_path = yammer_data_path
    with open(output_path, 'w') as file:
        json.dump(messages, file, indent=4)

if not os.path.exists(sentiment_pairs_path):
    with open(yammer_data_path, 'r') as f:
        documents = json.loads(f.read())

    sentiment_key_words_pairs = process_documents_in_batches(documents)

    with open(sentiment_pairs_path, 'w') as file:
        json.dump(sentiment_key_words_pairs, file, indent=4)


with open(sentiment_pairs_path, 'r') as file:
    data_from_file = json.load(file)

from collections import defaultdict
phrase_dict = defaultdict(str)

for item in data_from_file:
    sentiment = item['sentiment']
    phrases = item['key_phrases']
    phrase_dict[sentiment] += " ".join(phrases) + " "

# Set up a figure for plotting all word clouds together
plt.figure(figsize=(20, 10))

subplot_index = 1
n_subplots = len([sentiment for sentiment in phrase_dict if phrase_dict[sentiment]])

for sentiment, aggregated_phrases in phrase_dict.items():
    if aggregated_phrases:  # Only proceed if there are phrases for this sentiment
        wordcloud = WordCloud(width=800, height=800, 
                              background_color='white', 
                              min_font_size=10).generate(aggregated_phrases)

        # Add a new subplot for each sentiment
        ax = plt.subplot(1, n_subplots, subplot_index)
        plt.imshow(wordcloud, interpolation="bilinear")
        
        plt.title(f"{sentiment.capitalize()} Sentiment", fontsize=20, pad=20)
        
        plt.axis("off")

        # Move to the next subplot position
        subplot_index += 1

# Adjust layout to prevent overlap and ensure clear division
plt.tight_layout(pad=3.0)
plt.show()


    