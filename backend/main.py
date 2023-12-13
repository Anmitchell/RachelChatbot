# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse # using to send audio file back
from fastapi.middleware.cors import CORSMiddleware
from decouple import config # Allows access to environment variables in .env file
import openai


# Custom Function Imports
from functions.openai_requests import convert_audio_to_text

# Initiating App
app = FastAPI()

# CORS - Origins -> dictates what domain URL's are excepted in back-end
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000"
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
) 

@app.get("/health")
async def check_health():
    return {"message": "I am healthy"}

#
@app.get("/post-audio-get/")
async def get_audio():

    # Get saved audio
    audio_input = open("voice.mp3", "rb") # read bytes for audio file

    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)

    print(message_decoded)

    return "Done"


# Post bot response
# Note: Not playing in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):
#     print("hello")