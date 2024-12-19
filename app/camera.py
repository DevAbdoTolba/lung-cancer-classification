import cv2
from emotion_recognition import predict_emotion

def gen_frames():
    camera = cv2.VideoCapture(0)  # Use 0 for web camera
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            emotion = predict_emotion(frame)
            # Display the emotion label on the frame
            cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2, cv2.LINE_AA)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.release()