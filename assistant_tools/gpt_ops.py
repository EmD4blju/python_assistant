import openai
import dotenv as env
import conf as assistant_config

credentials_config = env.dotenv_values('credentials/.env')
openai.api_key = credentials_config.get('API_KEY')
assistant_rules = assistant_config.get('assistant_rules')

message_log = [
    {
        'role': 'system',
        'content': assistant_rules
    }
]

def get_completion(prompt:str, model='gpt-3.5-turbo') -> str: # [Notice]: communicates with OpenAI API
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