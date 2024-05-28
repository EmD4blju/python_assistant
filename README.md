# Private assistant #

### Requirements
* Check [requirements](requirements.txt)
* OpenAI api key
* Google Cloud json keys: (tts.json, s2t.json)
* OpenWeather api key

### How to set up
* To download required libraries just run the following cmd command:
```
pip install -r requirements.txt
```
* Create a directory "credentials" with items:
  * .env:
    * API_KEY: (OpenAi api key)
    * W_API_KEY: (OpenWeather api key)
    * TTS_PATH: (path to Google Cloud tts.json key)
    * S2T_PATH: (path to Google Cloud s2t.json key)


### How to run
* In the project directory, run the following cmd command:

```
python app.py --config "assistant_config.yaml"
```

### How it works
* \[ASSISTANT\]: Listetning... - your turn to talk
* \[USER\]: (content) - your sentence
* \[ASSISTANT\]: (content) - assistant's response

#### Functionalities
* Try asking for a weather specifying the city
* Ask for some information on Wikipedia
* Ask for anything (It is powered by gpt-3.5-turbo)
* A log of current running conversation is being built 
which enables the assitant to "remember"

### Notice
* The assistant is currently Polish exclusive
* [Configuration file](assistant_config.yaml) 
can be modified for the model to behave differently, 
however this might disable some of its functions