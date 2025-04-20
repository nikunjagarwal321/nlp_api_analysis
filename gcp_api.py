import requests
import json
from api_key import GOOGLE_API_KEY  # Make sure this file contains GOOGLE_API_KEY = "..."

# ========================
# GOOGLE NLP FUNCTIONS
# ========================

def analyze_google_sentiment(text):
    url = f"https://language.googleapis.com/v2/documents:analyzeSentiment?key={GOOGLE_API_KEY}"
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": text
        },
        "encodingType": "UTF8"
    }
    response = requests.post(url, json=payload)
    return response.json()

def analyze_google_entities(text):
    url = f"https://language.googleapis.com/v2/documents:analyzeEntities?key={GOOGLE_API_KEY}"
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": text
        },
        "encodingType": "UTF8"
    }
    response = requests.post(url, json=payload)
    return response.json()

def classify_google_text(text):
    url = f"https://language.googleapis.com/v2/documents:classifyText?key={GOOGLE_API_KEY}"
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": text
        }
    }
    response = requests.post(url, json=payload)
    return response.json()

# ========================
# PROCESS AND STORE RESULTS
# ========================

def analyze_and_store(data, content_type, results):
    for entry in data.get(content_type, []):
        try:
            sentiment_response = analyze_google_sentiment(entry)
        except Exception as e:
            print(f"Error analyzing sentiment for {content_type}: {e}")
            sentiment_response = None

        try:
            entities_response = analyze_google_entities(entry)
        except Exception as e:
            print(f"Error analyzing entities for {content_type}: {e}")
            entities_response = None

        try:
            categories_response = classify_google_text(entry)
        except Exception as e:
            print(f"Error classifying categories for {content_type}: {e}")
            categories_response = None

        print(f"Sentiment ({content_type}):", sentiment_response)
        print("Entities:", entities_response)
        print("Categories:", categories_response)
        print("-----------------------------------------------------")

        results.append({
            'type': content_type,
            content_type: entry,
            'sentiment': sentiment_response,
            'entities': entities_response,
            'categories': categories_response
        })

# ========================
# MAIN SCRIPT
# ========================

with open('./data/input.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []
for section in ['articles', 'comments', 'reviews']:
    print(f"Analyzing {section}...")
    analyze_and_store(data, section, results)

with open('./data/gcp_output.json', 'w', encoding='utf-8') as output_file:
    json.dump(results, output_file, ensure_ascii=False, indent=4)
