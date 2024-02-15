import os
import subprocess
from gtts import gTTS
import speech_recognition as sr
from .clean_text import clean_text
from .play_audio import play_audio

def text_to_speech(text):
    cleaned_text = clean_text(text)
    tts = gTTS(text=cleaned_text, lang='en', slow=False)
    
    audio_path = "output/audio/output.mp3"
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    tts.save(audio_path)
    tts.save(audio_path)
    play_audio(audio_path)