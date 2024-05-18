import wave
import playsound as ps
import speech_recognition as sr
import wikipedia_bs4 as wbs4
import speech_ops
import gpt_ops


def recordAudio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = sr.Recognizer().listen(source)
    return audio

def run():
    response_param = 0
    while True:
        try:
            response_param += 1
            wav_file = recordAudio().get_wav_data()
            with wave.open("sounds/my_sound.wav", "wb") as sound_file:
                print("Saving to file...")
                sound_file.setnchannels(1)
                sound_file.setsampwidth(2)
                sound_file.setnframes(48000)
                sound_file.setframerate(48000)
                sound_file.writeframes(wav_file)
            prompt = speech_ops.speech_to_text("sounds/my_sound.wav")
            print(prompt)
            response = gpt_ops.get_completion(prompt)
            print(response)
            if response == 'stop':
                return
            elif response.startswith('check_wiki'):
                response = wbs4.search_wikipedia(response.split(' ')[1])
            speech_ops.text_to_speech(response, response_param)
            ps.playsound(f"sounds/assistant_log/assistant_sound_{response_param}.wav")
        except:
            print("Processing your query has failed, please try again.")

if __name__ == '__main__':
    run()