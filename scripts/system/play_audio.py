import pygame
import time
import os

def play_audio(audio_path):
    if not os.path.exists(audio_path):
        print(f"File not found: {audio_path}")
        return

    # 1. Initialize
    pygame.mixer.init()

    try:
        # 2. Load and Play
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        # 3. Wait for it to finish
        while pygame.mixer.music.get_busy():
            time.sleep(0.1) # Shorter sleep for better responsiveness

        # 4. CRITICAL: Stop and Unload the file
        pygame.mixer.music.stop()
        pygame.mixer.music.unload() # Releases the file handle

    finally:
        # 5. CRITICAL: Shut down the mixer to release the ALSA device
        pygame.mixer.quit()

    # 6. Cleanup
    try:
        os.remove(audio_path)
    except Exception as e:
        print(f"Error while removing file: {e}")
