import transformers
import tensorflow as tf
import logging
import json

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

def generate_text(prompt, model, tokenizer, settings_path="settings.json"):
    with open(settings_path, "r") as settings_file:
        settings = json.load(settings_file)

    max_length = settings.get("max_length", 50)

    inputs = tokenizer.encode(prompt, return_tensors="tf", max_length=max_length, truncation=True)
    attention_mask = tf.ones_like(inputs)
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_beams=5,
        no_repeat_ngram_size=2,
        top_k=50,
        top_p=None,
        do_sample=True,
        attention_mask=attention_mask
    )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text