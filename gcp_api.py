import requests
import json

# ========================
# CONFIGURATION VARIABLES
# ========================

# GOOGLE CLOUD CONFIG
GOOGLE_API_KEY = ""

# Sample input text
TEXT_INPUT = "The new iPhone has great features but is too expensive for most people."


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

print(analyze_google_sentiment(TEXT_INPUT))
print(analyze_google_entities(TEXT_INPUT))
print(classify_google_text(TEXT_INPUT))
# ========================
