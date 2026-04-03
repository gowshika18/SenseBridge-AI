from flask import Flask, render_template, request, jsonify

from object_detection import detect_objects
from speech_to_text import listen_speech
from text_to_speech import speak_text

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speech-to-text')
def speech_to_text():
    text = listen_speech()
    return jsonify({"text": text})

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    result = speak_text(data['text'])
    return jsonify({"status": result})

@app.route('/detect')
def detect():
    result = detect_objects()
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
