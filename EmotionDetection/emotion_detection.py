"""Flask server for emotion detection application."""
import requests 
import json

def emotion_detector(text_to_analyse):

    if not text_to_analyse.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }


    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url,json = myobj, headers = header)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    response_dict = json.loads(response.text)
    emotion_data = response_dict['emotionPredictions'][0]['emotion']

    emotion_data["dominant_emotion"] = max(emotion_data, key=lambda k: emotion_data[k])

    return emotion_data
    