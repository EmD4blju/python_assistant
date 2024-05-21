from google.cloud import speech
from google.cloud import texttospeech
import dotenv as env
import os

config = env.dotenv_values("credentials/.env")

def speech_to_text(file_name) -> str: # [Notice]: function converts speech to text
    client = speech.SpeechClient.from_service_account_file(config.get('S2T_PATH'))
    with open(file_name, 'rb') as file:
        wav_data = file.read()
    response = client.recognize(
        config=speech.RecognitionConfig(language_code='pl-PL'), # TODO: update that config (might work better)
        audio=speech.RecognitionAudio(content=wav_data)
    )
    return response.results[0].alternatives[0].transcript

def text_to_speech(text, file_no): # [Notice]: function converts text to speech
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.get('TTS_PATH')
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
    with open(f'sounds/assistant_log/assistant_sound_{file_no}.wav', 'wb') as sound_file:
        sound_file.write(response.audio_content)