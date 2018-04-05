from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, learn Python in 4 hours!'


@app.route('/python')
def python():
    return 'Learn Python easily.'


@app.route('/video/<int:video_id>')
def show_video(video_id):
    return 'Showing video {}'.format(video_id)
