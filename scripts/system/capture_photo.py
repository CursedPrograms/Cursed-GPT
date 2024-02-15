import os
import cv2

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