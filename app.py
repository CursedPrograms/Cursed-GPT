from flask import Flask, render_template, request
import transformers
from transformers import TFAutoModelForCausalLM, AutoTokenizer
import tensorflow as tf
import logging

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

app = Flask(__name__)

model_name = "gpt2"
model = TFAutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, pad_token_id=50256)

def generate_text(prompt, model, tokenizer, max_length=50):
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

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    generated_text = generate_text(prompt, model, tokenizer)
    return render_template('index.html', prompt=prompt, generated_text=generated_text)

if __name__ == '__main__':
    app.run(debug=True)
