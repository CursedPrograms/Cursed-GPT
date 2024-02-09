import transformers
from transformers import TFAutoModelForCausalLM, AutoTokenizer
from gtts import gTTS
import subprocess
import tensorflow as tf
import logging
import os
from bs4 import BeautifulSoup
import cv2
import time
import numpy as np
import pyaudio
import speech_recognition as sr
import wave
from generate_text import generate_text

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

import urllib.request

def download_file(url, save_path):
    urllib.request.urlretrieve(url, save_path)

def download_caffe_model_files():
    # Create a directory to save the model files
    os.makedirs("models", exist_ok=True)

    # Download deploy.prototxt
    deploy_prototxt_url = "https://github.com/chuanqi305/MobileNet-SSD/raw/master/deploy.prototxt"
    deploy_prototxt_path = os.path.join("models", "deploy.prototxt")
    download_file(deploy_prototxt_url, deploy_prototxt_path)

    # Download mobilenet_iter_73000.caffemodel
    caffemodel_url = "https://github.com/chuanqi305/MobileNet-SSD/raw/master/mobilenet_iter_73000.caffemodel"
    caffemodel_path = os.path.join("models", "mobilenet_iter_73000.caffemodel")
    download_file(caffemodel_url, caffemodel_path)

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
    audio_path = "output/audio/output.mp3"
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    tts.save(audio_path)

    # Open the audio file with the default media player
    try:
        subprocess.run(["start", audio_path], check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def capture_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

def capture_audio(duration=5, sample_rate=44100):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)

    frames = []
    print("Recording audio...")

    for i in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

    # Save audio data to a temporary file
    
    temp_audio_file = "output/audio/temp_audio.wav"
    os.makedirs(os.path.dirname(temp_audio_file), exist_ok=True)
    wf = wave.open(temp_audio_file, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    return temp_audio_file

def capture_photo(output_dir="output/shot"):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open a connection to the webcam
    cap = cv2.VideoCapture(0)

    # Capture a single frame
    ret, frame = cap.read()

    # Release the webcam
    cap.release()

    # Save the captured frame to the specified directory
    image_path = os.path.join(output_dir, "captured_photo.jpg")
    cv2.imwrite(image_path, frame)

    return image_path

def image_description(image_path):
    # Load the pre-trained MobileNet SSD model and its class labels
    net = cv2.dnn.readNetFromCaffe("models/deploy.prototxt", "models/mobilenet_iter_73000.caffemodel")
    classes = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair",
               "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa",
               "train", "tvmonitor"]

    # Load and preprocess the input image
    image = cv2.imread(image_path)
    h, w = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 0.007843, (300, 300), 127.5)

    # Pass the blob through the network and obtain the detections
    net.setInput(blob)
    detections = net.forward()

    # Loop over the detections and get the description of the most confident prediction
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:  # Confidence threshold
            class_id = int(detections[0, 0, i, 1])
            description = f"A photo containing a {classes[class_id]} with confidence {confidence:.2f}"
            return description

    return "Unable to identify the content of the photo."

if not os.path.exists("models/deploy.prototxt") or not os.path.exists("models/mobilenet_iter_73000.caffemodel"):
    download_caffe_model_files()

# Example usage:
captured_image_path = capture_photo()
print(f"Captured image saved at: {captured_image_path}")

description = image_description(captured_image_path)
print(description)

def main():
    model_name = "gpt2"
    model = TFAutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name, pad_token_id=50256)

    while True:
        # Capture a photo and get image description
        photo = capture_photo()
        image_desc = image_description(photo)
        print(f"Image Description: {image_desc}")

        # Convert audio file to text
        recognizer = sr.Recognizer()
        audio_text = ""

        with sr.AudioFile(capture_audio()) as source:
            try:
                audio = recognizer.record(source)
                audio_text = recognizer.recognize_google(audio)
                print(f"Audio Text: {audio_text}")
            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Error with the speech recognition service; {e}")

        # Determine the prompt based on available information
        if audio_text and image_desc:
            prompt = f"{audio_text} {image_desc}"
        elif audio_text:
            prompt = audio_text
        elif image_desc:
            prompt = image_desc
        else:
            prompt = ""

        # Generate text based on the prompt
        generated_text = generate_text(prompt, model, tokenizer)

        # Print and say the generated text
        if generated_text:
            print("Generated Text:")
            print(generated_text)
            text_to_speech(generated_text)

        # Sleep for 15 seconds before the next iteration
        time.sleep(15)

if __name__ == "__main__":
    main()