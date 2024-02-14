import transformers
from transformers import TFAutoModelForCausalLM, AutoTokenizer
import tensorflow as tf
import logging
import os
import cv2
import time
import numpy as np
import pyaudio
import speech_recognition as sr
import wave
from system.generate_text import generate_text
from system.tts import text_to_speech
from system.capture_photo import capture_photo
from system.greeting import greeting

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

import urllib.request

greeting()

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
            description = f"a {classes[class_id]}"
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
        text_to_speech(f"I see a: {image_desc}")
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
        if generated_text:
            print("Generated Text:")
            print(generated_text)
            text_to_speech(generated_text)

        # Sleep for 15 seconds before the next iteration
        time.sleep(15)

if __name__ == "__main__":
    main()