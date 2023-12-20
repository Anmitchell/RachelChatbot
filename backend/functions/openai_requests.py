import openai
from decouple import config

# Import custom functions
from functions.database import get_recent_messages

# Retrieve Environment Variables
openai.orginization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

# OpenAI - Whisper -> convert audio to text
def convert_audio_to_text(audio_file):
    try:
        # audio_file = open("voice.mp3", "rb") # read file in bytes
        transcript = openai.audio.transcriptions.create(
            model = "whisper-1",
            file = audio_file,
            response_format = "text"
        )
        return transcript
    except Exception as e:
        print(e)
        return e

# Open AI - ChatGPT
# Get Response to our Message
def get_chat_response(message_input):

    # message recieved from AI
    # message input given from decoded audio file 
    # add user message to list of recent messages
    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)
    print(messages) # print message to console for debugging

    try:
        response = openai.chat.completions.create( # is not defined ?
            model = "gpt-4",
            messages = messages,
        )

        # print(response)
        # Message recieved by chatGPT (AI):
        # Object is returned by chatBPT and the property choices is an array of objects
        # message is the first object in the array, the content property of message is returned
        message_text = response.choices[0].message.content
        return message_text
    except Exception as e:
        print(e)
        return
