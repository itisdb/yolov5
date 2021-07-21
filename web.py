#Import necessary libraries
from flask import Flask, render_template, Response
import detect as yolo
import argparse

def flask(
    src='0' #change this to your rtsp/rtmp/https stream
    ):
    #Initialize the Flask app
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/video_feed')
    def video_feed():
        return Response(yolo.run(source=src,view_img=True), mimetype='multipart/x-mixed-replace; boundary=frame')

    app.run(debug=True, host='0.0.0.0', port=8080)

def parse_opt():
    parser = argparse.ArgumentParser(description='[+] YOLO V5 Object Detection : @itisdb')
    parser.add_argument('--src', type=str, default='0',
                        help='Video Source, e.g. rtsp://admin:')
    return parser.parse_args()

def main(args):
    flask(args.src)

if __name__ == '__main__':
    args = parse_opt()
    main(args)