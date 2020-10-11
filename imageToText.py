import json
import os
import sys
import requests
import time
from PIL import Image
from io import BytesIO

def imageToText(img):
    missing_env = False
    if 'COMP_VIS_ENDPOINT' in os.environ:
        endpoint = os.environ['COMP_VIS_ENDPOINT']
    else:
        print("Azure subscription key and/or endpoint not found in evnrionment variables")
        print("Retrieve these from your Azure dashboard")
        missing_env = True

    if 'COMP_VIS_SERVICE_KEY' in os.environ:
        subscription_key = os.environ['COMP_VIS_SERVICE_KEY']
    else:
        print("Azure subscription key and/or endpoint not found in evnrionment variables")
        print("Retrieve these from your Azure dashboard")
        missing_env = True

    if missing_env:
        sys.exit()

    ocr_url = endpoint + "/vision/v3.0/read/analyze"

    image_path = img
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    response = requests.post(ocr_url, headers=headers, data = image_data)
    response.raise_for_status()

    operation_url = response.headers["Operation-Location"]

    analysis = {}
    poll = True
    while (poll):
        response_final = requests.get(
            response.headers["Operation-Location"], headers=headers)
        analysis = response_final.json()
        time.sleep(1)
        if ("analyzeResult" in analysis):
            poll = False
        if ("status" in analysis and analysis['status'] == 'failed'):
            poll = False

    runningSent = ''
    for elem in analysis['analyzeResult']['readResults'][0]['lines']:
        runningSent += (' ' + elem['text'])
    
    return runningSent