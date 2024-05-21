import openai
import dotenv as env

config = env.dotenv_values("credentials/.env")
openai.api_key = config.get("API_KEY")

# TODO: Upgrade this fucking prompt, cause the model is stupid
initial_prompt = f"""
    Nazywasz się EM.K4
    Staniesz się narzędziem, którego celem jest udzielenie odpowiedzi:
    check_weather lub check_wiki lub stop
    Rzecz w tym, że Twoja odpowiedź powinna być adekwatna do tego, o co pyta użytkownik.
    Użytkownik może mówić w innym języku, zawsze odpowiadaj w tym języku.
    Jeśli nic nie pasuje, po prostu porozmawiaj na ten temat z użytkownikiem
    Oto kilka zasad, których musisz przestrzegać:
      - Jeśli użytkownik zapyta o informacje na jakiś temat, odpowiedz w następującym formacie:
            check_wiki pełny_link
      - Pamiętaj, aby wkleić pełny link do Wikipedii, tak aby był zgodny z prośbą użytkownika.
      - Po spacji należy podać wyłącznie link dla użytkownika.
      - Również jeśli chodzi o pogodę, pamiętaj o wpisaniu właściwej lokalizacji, wystarczy tylko miasto.
      - Jeśli nie znasz lokalizacji, po prostu poproś o nią użytkownika.
      - Twoja odpowiedź powinna być możliwie krótka i prosta, bez zbędnych komentarzy itp.
      - Jeśli użytkownik powie stop, po prostu odpowiadasz stop, bez żadnych komentarzy (TO JEST WAŻNE!!!!)
"""

message_log = [
    {
        'role': 'system',
        'content': initial_prompt
    }
]

def get_completion(prompt:str, model="gpt-3.5-turbo") -> str: # [Notice]: communicates with OpenAI API
    message_log.append({
        'role': 'user',
        'content': prompt
    })
    response = openai.chat.completions.create(
        model=model,
        messages=message_log
    ).choices[0].message.content
    message_log.append({
        'role': 'assistant',
        'content': response
    })
    return response