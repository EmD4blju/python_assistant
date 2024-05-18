import asyncio
import wave
import playsound as ps
import audio_recorder as ar
import wikipedia_bs4 as wbs4
import weather_ops as wo
import speech_ops
import gpt_ops


user_sound_path = 'sounds/my_sound.wav'

# TODO: run() function needs to be divided
#  into smaller functions for code readability
async def run():
    file_no = 0
    while True:
        file_no += 1
        try:
            wav_frames = ar.record_audio().get_wav_data()
            with wave.open(user_sound_path, "wb") as sound_file:
                # print("Saving to file...")
                sound_file.setnchannels(1)
                sound_file.setsampwidth(2)
                sound_file.setnframes(48000)
                sound_file.setframerate(48000)
                sound_file.writeframes(wav_frames)
            prompt = speech_ops.speech_to_text(user_sound_path)
            print('[USER]: ', prompt, sep='\t')
            response = gpt_ops.get_completion(prompt)
            print('[ASSISTANT]: ', response, sep='\t')
            if response == 'stop': return
            elif response.startswith('check_wiki'): response = wbs4.search_wikipedia(response.split(' ')[1]) # WILL BE JSON
            elif response.startswith('check_weather'): response = await wo.get_weather(response.split(' ')[1]) # JSON
            speech_ops.text_to_speech(response, file_no)
            ps.playsound(f"sounds/assistant_log/assistant_sound_{file_no}.wav")
        except:
            error = "Przepraszam, nie rozumiem co powiedziałeś, możesz powtórzyć?"
            print('[ASSISTANT]:', error, sep='\t')
            ps.playsound('sounds/assistant_log/assistant_sound_error.wav')


if __name__ == '__main__':
    asyncio.run(run())