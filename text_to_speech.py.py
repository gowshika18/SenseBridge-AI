import pyttsx3

engine = pyttsx3.init()

# Optional: adjust voice properties
engine.setProperty('rate', 150)   # speed
engine.setProperty('volume', 1.0) # volume


def speak_text(text):
    try:
        engine.say(text)
        engine.runAndWait()
        return "Spoken successfully"
    except Exception as e:
        return f"Error: {str(e)}"