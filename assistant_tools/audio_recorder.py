import speech_recognition as sr
def record_audio() -> sr.AudioData: # [Notice]: function records user audio
    with sr.Microphone() as source:
        print("[ASSISTANT]: Listening...")
        audio = sr.Recognizer().listen(source)
    return audio