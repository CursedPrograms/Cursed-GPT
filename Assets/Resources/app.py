from flask import Flask, render_template, request
import transformers
from transformers import TFAutoModelForCausalLM, AutoTokenizer
import tensorflow as tf
import logging
from scripts.system.generate_text import generate_text
import webbrowser

transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

app = Flask(__name__, static_url_path='/static')

model_name = "gpt2"
model = TFAutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, pad_token_id=50256)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    generated_text = generate_text(prompt, model, tokenizer)
    return render_template('index.html', prompt=prompt, generated_text=generated_text)

if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True, use_reloader=False)
