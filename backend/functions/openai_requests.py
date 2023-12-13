import openai
from decouple import config

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

