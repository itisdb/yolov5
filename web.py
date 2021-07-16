#Import necessary libraries
from flask import Flask, render_template, Response
import cv2
import os
from Yolo_Demo_WCF import YOLO_OBJECT_DETECTION

#Initialize the Flask app
app = Flask(__name__)
source=0   #change this source when changing every stuff.
camera = cv2.VideoCapture(source)
'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)

#this is for the generator function of the app when just live stream
def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        #ret, buffer=yolo.run(source=frame)
        #buffer=YOLO_OBJECT_DETECTION(True,frame)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(YOLO_OBJECT_DETECTION(True,source), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)