import wave
from assistant_tools import audio_recorder as ar, wikipedia_bs4 as wbs4, gpt_ops, speech_ops, weather_ops as wo
from pydub import AudioSegment
from pydub.playback import play

def write_wav_frames(wav_frames) -> None: # [Notice]: function writes .wav frames into a file
    with wave.open('sounds/my_sound.wav', 'wb') as sound_file:
        sound_file.setnchannels(1) # 1-channeled microphone
        sound_file.setsampwidth(2) # 2 bytes (16 bits) microphone
        sound_file.setnframes(48000) # 48 kHz
        sound_file.setframerate(48000) # 48 kHz
        sound_file.writeframes(wav_frames)

def perform_error() -> None: # [Notice]: function performs a communication whenever error occurred
    error = 'Przepraszam, nie rozumiem co powiedziałeś, możesz powtórzyć?'
    print('[ASSISTANT]:', error, sep='\t')
    play(AudioSegment.from_wav('sounds/assistant_sound_error.wav'))

def perform_chat() -> str: # [Notice]: function performs a communication with OpenAI language model
    prompt = speech_ops.speech_to_text('sounds/my_sound.wav')
    print('[USER]: ', prompt, sep='\t')
    response = gpt_ops.get_completion(prompt)
    print('[ASSISTANT]: ', response, sep='\t')
    if response == 'stop':
        return 'stop'
    elif response.startswith('check_wiki'):
        response = wbs4.search_wikipedia(response.split(' ')[1])
    elif response.startswith('check_weather'):
        response = wo.get_weather(response.split(' ')[1])
    return response

def run() -> None: # main method of the assistant app
    while True:
        try:
            wav_frames = ar.record_audio().get_wav_data() # records audio
            write_wav_frames(wav_frames) # writes recorded audio to a file
            response = perform_chat() # provides response from performed chat if response == 'stop': return
            if response == 'stop': return
            speech_ops.text_to_speech(response) # converts response to audio, writes to a file of file_no
            play(AudioSegment.from_wav('sounds/assistant_sound.wav'))
        except:
            perform_error()


if __name__ == '__main__':
    run()