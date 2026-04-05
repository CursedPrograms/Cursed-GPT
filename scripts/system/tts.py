import os
import pyttsx3
from gtts import gTTS
from .clean_text import clean_text
from .play_audio import play_audio

def text_to_speech(text):
    cleaned_text = clean_text(text)
    audio_path = "output/audio/output.mp3"
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    try:
        # Attempt Google TTS (High Quality)
        tts = gTTS(text=cleaned_text, lang='en', slow=False)
        tts.save(audio_path)
        play_audio(audio_path)

    except Exception as e:
        print(f"\n[!] Voice Connection Failed: {e}")
        print("[!] Falling back to local system voice...")

        # Fallback to local offline TTS
        engine = pyttsx3.init()
        # Optional: Adjust rate/volume to match Friday's vibe
        engine.setProperty('rate', 175)
        engine.say(cleaned_text)
        engine.runAndWait()
