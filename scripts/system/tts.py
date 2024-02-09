import os
import subprocess
from gtts import gTTS
import speech_recognition as sr
from .clean_text import clean_text

def text_to_speech(text):
    cleaned_text = clean_text(text)
    tts = gTTS(text=cleaned_text, lang='en', slow=False)
    
    audio_path = "output/audio/output.mp3"
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    tts.save(audio_path)

    # Open the audio file with the default media player
    try:
        subprocess.run(["start", audio_path], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")