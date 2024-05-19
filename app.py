import asyncio
import sys
import wave
import playsound as ps
import audio_recorder as ar
import wikipedia_bs4 as wbs4
import weather_ops as wo
import speech_ops
import gpt_ops

def write_wav_frames(wav_frames) -> None: # [Notice]: function writes .wav frames into a file
    with wave.open('sounds/my_sound.wav', "wb") as sound_file:
        sound_file.setnchannels(1) # 1-channeled microphone
        sound_file.setsampwidth(2) # 2 bytes (16 bits) microphone
        sound_file.setnframes(48000) # 48 kHz
        sound_file.setframerate(48000) # 48 kHz
        sound_file.writeframes(wav_frames)

def perform_error() -> None: # [Notice]: function performs a communication whenever error occurred
    error = "Przepraszam, nie rozumiem co powiedziałeś, możesz powtórzyć?"
    print('[ASSISTANT]:', error, sep='\t')
    ps.playsound('sounds/assistant_log/assistant_sound_error.wav')

async def perform_chat() -> str: # [Notice]: function performs a communication with OpenAI language model
    prompt = speech_ops.speech_to_text('sounds/my_sound.wav')
    print('[USER]: ', prompt, sep='\t')
    response = gpt_ops.get_completion(prompt)
    print('[ASSISTANT]: ', response, sep='\t')
    if response == 'stop':
        return 'stop'
    elif response.startswith('check_wiki'):
        response = wbs4.search_wikipedia(response.split(' ')[1]) # TODO: needs json
    elif response.startswith('check_weather'):
        response = await wo.get_weather(response.split(' ')[1]) # TODO: json needs to be formatted to a readable string
    return response

async def run() -> None: # main method of the assistant app
    file_no = 0 # TODO: Can it be placed somewhere else?
    while True:
        file_no += 1 # TODO: Can it be placed somewhere else?
        try:
            wav_frames = ar.record_audio().get_wav_data() # records audio
            write_wav_frames(wav_frames) # writes recorded audio to a file
            response = await perform_chat() # provides response from performed chat
            if response == 'stop': return
            speech_ops.text_to_speech(response, file_no) # converts response to audio, writes to a file of file_no
            ps.playsound(f"sounds/assistant_log/assistant_sound_{file_no}.wav") # uses an example of file of file_no
        except:
            perform_error()


if __name__ == '__main__':
    asyncio.run(run())