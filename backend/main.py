from fastapi import FastAPI, UploadFile, File # what do UploadFile and File do?
from fastapi.middleware.cors import CORSMiddleware
from fer import FER
import cv2
import numpy as np

app = FastAPI()

# Enable Cors if frontend is on another port
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

# Load FER model
emotion_detector = FER()

# convert bytes to image, process emotion and score, send them back
@app.post('/detect')
async def detect(file: UploadFile = File(...)):
    contents = await file.read()
    np_img = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    emotions = emotion_detector.detect_emotions(img)

    if emotions:
        dominant_emotion = emotion_detector.top_emotion(img)
        return{'emotion': dominant_emotion[0],
               'score': dominant_emotion[1]}
    else:
        return {'emotion': 'no face detected', 'score': 0.0}
    
