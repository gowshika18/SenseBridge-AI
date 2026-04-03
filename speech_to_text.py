import speech_recognition as sr

def listen_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            return text
        except:
            return "Error recognizing speech"
