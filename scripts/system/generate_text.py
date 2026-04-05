import transformers
import tensorflow as tf
import logging
import json

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

def generate_text(prompt, model, tokenizer, settings_path="settings.json"):
    with open(settings_path, "r") as settings_file:
        settings = json.load(settings_file)

    max_length = settings.get("max_length", 100) # Increased for better flow

    inputs = tokenizer.encode(prompt, return_tensors="tf", max_length=max_length, truncation=True)

    # We create the attention mask explicitly to help the model stay on track
    attention_mask = tf.ones_like(inputs)

    outputs = model.generate(
        inputs,
        max_length=max_length,
        do_sample=True,             # Keep this True
        top_k=50,                   # Good for diversity
        top_p=0.92,                 # Changed from None: This is Nucleus Sampling
        temperature=0.8,            # Added: Controls 'randomness' (0.7-0.9 is best)
        no_repeat_ngram_size=3,     # Increased to 3 to prevent loops like "the the the"
        repetition_penalty=1.2,     # Added: Discourages the model from repeating itself
        attention_mask=attention_mask,
        pad_token_id=tokenizer.eos_token_id
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
