import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
import json

def getEmotion():
    # Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
    KEY = os.environ['FACE_SUBSCRIPTION_KEY']

    # Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
    ENDPOINT = os.environ['FACE_ENDPOINT']

    headers = {'Ocp-Apim-Subscription-Key': KEY,
            'Content-Type': 'application/octet-stream'}

    params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion,gender,headPose,smile,facialHair,glasses,age,hair,makeup,occlusion,accessories,blur,exposure,noise',
        }

    # Read the local image into a byte array
    filename = ""
    f = open(filename, "rb")
    body = f.read()
    f.close()

    body = body

    try:
        # Execute the REST API call and get the response.
        response = requests.request('POST', ENDPOINT + '/face/v1.0/detect', data=body, headers=headers,
                                    params=params)
        parsed = json.loads(response.text)
        print(parsed)
        age = parsed[0]['faceAttributes']["emotion"]
        #?????not sure how to fix this ;-;
        return(emotion)


    except Exception as e:
        print('Error:')
        print(e)

    """
    for face in detected_faces:
        attributes = face.FaceAttributes
        print(attributes.Emotion)


    # Display the detected face ID in the first single-face image.
    # Face IDs are used for comparison to faces (their IDs) detected in other images.
    print('Detected face ID from', single_image_name, ':')
    for face in detected_faces: print (face.face_id)

    """
