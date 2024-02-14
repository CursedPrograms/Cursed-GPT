import transformers
from transformers import TFAutoModelForCausalLM, AutoTokenizer
import tensorflow as tf
import logging
from system.generate_text import generate_text
from system.tts import text_to_speech
from system.stt import speech_to_text

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

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
