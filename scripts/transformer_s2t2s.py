import transformers
from transformers import TFAutoModelForCausalLM, AutoTokenizer
from gtts import gTTS
import subprocess
import tensorflow as tf
import logging
import os
from bs4 import BeautifulSoup
import speech_recognition as sr
from generate_text import generate_text

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

def clean_text(text):
    # Remove HTML tags
    soup = BeautifulSoup(text, "html.parser")
    cleaned_text = soup.get_text(separator=" ")

    # Remove unwanted characters
    cleaned_text = cleaned_text.replace("\n", " ").strip()

    return cleaned_text

def text_to_speech(text):
    cleaned_text = clean_text(text)
    tts = gTTS(text=cleaned_text, lang='en', slow=False)
    
    audio_path = "../output/output.mp3"

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    tts.save(audio_path)

    # Open the audio file with the default media player
    try:
        subprocess.run(["start", audio_path], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        prompt = recognizer.recognize_google(audio)
        print(f"You said: {prompt}")
        return prompt
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
        return ""

def main():
    model_name = "gpt2"
    model = TFAutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name, pad_token_id=50256)

    while True:
        choice = input("Choose input method (1 for text, 2 for speech, 'exit' to end): ")

        if choice == '1':
            prompt = input("Enter a prompt: ")
        elif choice == '2':
            prompt = speech_to_text()
        elif choice.lower() == 'exit':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or 'exit'.")
            continue

        generated_text = generate_text(prompt, model, tokenizer)

        print("Generated Text:")
        print(generated_text)

        text_to_speech(generated_text)

if __name__ == "__main__":
    main()
