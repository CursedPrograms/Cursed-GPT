import json
from .tts import text_to_speech

def greeting(settings_path="settings.json"):
    with open(settings_path, "r") as settings_file:
        settings = json.load(settings_file)
    Name = settings.get("Name", "User")
    text = (f"Hello, I am {Name}, how can I help you?")
    print(text)
    text_to_speech(text)