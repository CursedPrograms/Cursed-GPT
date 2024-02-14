import pygame
import time
import os

def play_audio(audio_path):
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)

    play_count = 0
    while play_count < 1:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        pygame.mixer.music.stop()
        play_count += 1
    
    try:
        os.remove(audio_path)
    except Exception as e:
        print(f"Error while removing file: {e}")
