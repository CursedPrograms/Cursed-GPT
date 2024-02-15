import transformers
from transformers import TFAutoModelForCausalLM, AutoTokenizer
import tensorflow as tf
import logging
from system.generate_text import generate_text

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

def main():
    model_name = "gpt2"
    model = TFAutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name, pad_token_id=50256)

    while True:
        prompt = input("Enter a prompt (type 'exit' to end): ")
        
        if prompt.lower() == 'exit':
            print("Exiting the program.")
            break

        generated_text = generate_text(prompt, model, tokenizer)

        print("Generated Text:")
        print(generated_text)

if __name__ == "__main__":
    main()
