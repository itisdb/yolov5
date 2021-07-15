from flask import Flask,render_template,Response
import cv2
from Yolo_Demo_WCF import YOLO_OBJECT_DETECTION

app=Flask(__name__)
camera=cv2.VideoCapture('m3u8\\video.m3u8')

def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(YOLO_OBJECT_DETECTION(True,camera),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)