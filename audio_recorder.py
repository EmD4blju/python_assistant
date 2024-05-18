import speech_recognition as sr

# This one listens properly for the microphone input.
# Why even bother if this data goes to Google Cloud speech recognition?
def record_audio() -> sr.AudioData:
    with sr.Microphone() as source:
        print("[ASSISTANT]: Listening...")
        audio = sr.Recognizer().listen(source)
    return audio