#Import necessary libraries
from flask import Flask, render_template, Response
import cv2
import os
import detect as yolo
#Initialize the Flask app
app = Flask(__name__)

'''
camera = cv2.VideoCapture('Sample1.mp4')
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)


def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        #ret, buffer=yolo.run(source=frame)
        ret, buffer = cv2.imencode('.jpg', frame)
        
        if not success:
            break
        else:
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
'''


#Change this to your source file _ 0: webcam, or paste the rtsp url here
#src='your rtsp url here'
src='enter your rtsp/https/rtmp url'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(yolo.run(source=src,view_img=True), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)