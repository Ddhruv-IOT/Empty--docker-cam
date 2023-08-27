from flask import Flask, Response, render_template
import cv2
import os

ip_address = os.getenv("IP_ADDRESS")

app = Flask(__name__)

# Initialize the video capture
video_capture = cv2.VideoCapture(f"http://{ip_address}:8080/video")

def generate_frames():
    while True:
        success, frame = video_capture.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Live Video Stream</title>
    </head>
    <body>
        <img src="/video_feed" alt="Video Stream">
    </body>
    </html>
    '''

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')