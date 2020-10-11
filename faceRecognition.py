import json, os, requests

def imageToEmotion(img):
    if 'FACE_SUBSCRIPTION_KEY' in os.environ:
        subscription_key = os.environ['FACE_SUBSCRIPTION_KEY']
    else:
        print("Azure subscription key and/or endpoint not found in evnrionment variables")
        print("Retrieve these from your Azure dashboard")
        missing_env = True
    
    if 'FACE_ENDPOINT' in os.environ:
        endpoint = os.environ['FACE_ENDPOINT']
        face_api_url = endpoint + '/face/v1.0/detect'
    else:
        print("Azure subscription key and/or endpoint not found in evnrionment variables")
        print("Retrieve these from your Azure dashboard")
        missing_env = True

    params = {
	'detectionModel': 'detection_01',
	'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    'returnFaceId': 'true'
    }

    image_path = img
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type': 'application/octet-stream'}
    response = requests.post(face_api_url, params=params,
                            headers=headers, data=image_data)
    response.raise_for_status()
    
    emotionResults = response.json()[0]['faceAttributes']['emotion']

    maxVal = 0
    retEmo = None
    for key in emotionResults:
        if emotionResults[key] > maxVal:
            retEmo = key
            maxVal = emotionResults[key]
    
    return retEmo
