from google.cloud import speech
from google.cloud import texttospeech
import dotenv as env
import os

config = env.dotenv_values("credentials/.env")

# This Google Cloud s2t is a monumental shit.
def speech_to_text(file_name) -> str:
    client = speech.SpeechClient.from_service_account_file(config.get('S2T_PATH'))

    with open(file_name, 'rb') as file:
        wav_data = file.read()

    response = client.recognize(
        config=speech.RecognitionConfig(language_code='pl-PL'),
        audio=speech.RecognitionAudio(content=wav_data)
    )
    return response.results[0].alternatives[0].transcript

# This one is even bigger (probably the hugest shit I've seen)
# Can someone tell me why credential application differs between those APIs?
def text_to_speech(text, file_no):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.get("TTS_PATH")
    client = texttospeech.TextToSpeechClient()

    response = client.synthesize_speech(
        request={
            'input': texttospeech.SynthesisInput(text=text),
            'voice': texttospeech.VoiceSelectionParams(
                language_code='pl-PL',
                ssml_gender=texttospeech.SsmlVoiceGender.MALE
            ),
            'audio_config': texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16
            )
        }
    )

    # At least this one is cool. Uses flush() function on a file to flush the previous shit to the sewers.
    with open(f'sounds/assistant_log/assistant_sound_{file_no}.wav', 'wb') as sound_file:
        sound_file.write(response.audio_content)
        sound_file.flush()

# GOOGLE DOCUMENTATION IS FULL OF NOTHING