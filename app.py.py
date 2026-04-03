from flask import Flask, render_template, request, jsonify

from object_detection import detect_objects
from speech_to_text import listen_speech
from text_to_speech import speak_text
from number_plate import detect_number_plate

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# 🎤 Speech to Text
@app.route('/speech-to-text')
def speech_to_text():
    text = listen_speech()
    return jsonify({"text": text})


# 🔊 Text to Speech
@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    result = speak_text(data['text'])
    return jsonify({"status": result})


# 👁️ Object Detection
@app.route('/detect')
def detect():
    result = detect_objects()
    return jsonify({"result": result})


# 🚗 Number Plate Detection
@app.route('/number-plate')
def number_plate():
    result = detect_number_plate()
    return jsonify({"plate": result})


if __name__ == '__main__':
    app.run(debug=True)