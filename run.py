'''
This is a YOLO V5 Object detection Model custom trained to detect Fire and Smoke over streaming protocols like rtsp/rtmp/https etc.
This is also served using flask so that the output can be easily visualized in browser using simple URL format.

Simple Setup :

Download the latest release
Open the Folder in VSCode or any other preferred editor.
Change the streaming link as shown in the README
Write the following in the Terminal
python run.py --src='your stream url'
'''

# Imports
import os
import argparse


def run(
    src='0'
    ):
    bash1='python -m pip install -r requirements.txt'
    bash2='python web.py --src='+src
    os.system(bash1)
    os.system(bash2)

def parse_opt():
    parser = argparse.ArgumentParser(description='[+] YOLO V5 Object Detection Automated: @itisdb')
    parser.add_argument("--src", type=str, default='0', help="Stream URL")
    args = parser.parse_args()
    return args

def main(args):
    run(args.src)

if __name__ == '__main__':
    args = parse_opt()
    main(args)