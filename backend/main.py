# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse # using to send audio file back
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles # using to server static files for production
from fastapi.responses import HTMLResponse
from fastapi import Depends
from decouple import config # Allows access to environment variables in .env file
import openai
import uuid


# Custom Function Imports
from functions.database import store_messages, reset_messages
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.text_to_speech import convert_text_to_speech

# Initiating App
app = FastAPI()

# CORS - Origins -> dictates what domain URL's are excepted in back-end
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
    "http://localhost:3005"
]

# Mount the static files route built by front-end tool
app.mount("/static", StaticFiles(directory="../frontend/dist"), name="static")

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
) 

    # Serve main HTML file from frontend
@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    with open("../frontend/dist/index.html") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.get("/reset")
async def reset_converstion():
    reset_messages()
    return {"message": "Conversation reset"}

#
@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):
    unique_filename = str(uuid.uuid4())
    file_path = f"uploads/{unique_filename}.mp3"

    # Save file from frontend
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: Ensure message decoded
    if not message_decoded:
        return HTTPException(status_code = 400, detail = "Failed to decode audio")

    # Get ChatGPTResponse
    chat_response = get_chat_response(message_decoded)

    # Guard: Ensure chat response
    if not chat_response:
        return HTTPException(status_code = 400, detail = "Failed to get chat response")
    
    # Store Messages
    store_messages(message_decoded, chat_response)

    # print(chat_response) # use for debugging

    # Convert chat response to audio
    audio_output = convert_text_to_speech(chat_response)

    # Guard: Ensure audio output
    if not audio_output:
        return HTTPException(status_code = 400, detail = "Failed to get eleven labs audio response")

    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Return audio file
    return StreamingResponse(iterfile(), media_type="application/octet-stream")

    # return "done"