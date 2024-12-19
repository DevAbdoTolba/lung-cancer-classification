import cv2
import numpy as np
from tensorflow.keras.models import load_model
import app

# Load the trained model
model = load_model('models/model_accurate.h5')
emotion_labels = ['Angry', 'Contempt', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

def predict_emotion(frame):
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
        return 'No Face Detected'
    for (x, y, w, h) in faces:
        roi = frame[y:y+h, x:x+w]
        roi = cv2.resize(roi, (224, 224))
        roi = roi / 255.0
        roi = np.expand_dims(roi, axis=0)
        preds = model.predict(roi)
        emotion = emotion_labels[np.argmax(preds)]
        app.log_interaction(emotion)
        return emotion
    return 'No Face Detected'