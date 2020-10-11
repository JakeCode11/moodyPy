from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import os
import sys

def client_authenticate():
    missing_env = False
    
    if 'COMP_SENT_ANALYSIS_SERVICE_KEY' in os.environ:
        subscription_key = os.environ['COMP_SENT_ANALYSIS_SERVICE_KEY']
    else:
        print("Azure subscription key and/or endpoint not found in evnrionment variables")
        print("Retrieve these from your Azure dashboard")
        missing_env = True
    
    if 'COMP_SENT_ANALYSIS_ENDPOINT' in os.environ:
        endpoint = os.environ['COMP_SENT_ANALYSIS_ENDPOINT']
    else:
        print("Azure subscription key and/or endpoint not found in evnrionment variables")
        print("Retrieve these from your Azure dashboard")
        missing_env = True
    
    if missing_env:
        sys.exit()
    
    ta_credential = AzureKeyCredential(subscription_key)
    text_analytics_client = TextAnalyticsClient(
                            endpoint=endpoint,
                            credential=ta_credential
                            )
    return text_analytics_client

def sentiment_analysis(client, loadedtxt):
    text = [loadedtxt]
    response = client.analyze_sentiment(documents=text)[0]
    rating = None

    for idx, sentence in enumerate(response.sentences):
        rating = sentence.sentiment
    
    return str(rating)

