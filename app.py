import os
import sys

# --- THE MAGIC SHIELD: MUST BE AT THE TOP ---
os.environ["TF_USE_LEGACY_KERAS"] = "1"
import tensorflow as tf
import tf_keras as keras
sys.modules["keras"] = keras
# --------------------------------------------

from flask import Flask, render_template, request
import transformers
from transformers import TFAutoModelForCausalLM, AutoTokenizer
import logging
from scripts.system.generate_text import generate_text
import webbrowser

# Suppress the noise
transformers.logging.set_verbosity_error()
tf.get_logger().setLevel(logging.ERROR)

app = Flask(__name__, static_url_path='/static')

model_name = "gpt2"

# Now this will load without the 'NoneType' error
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
    # Note: debug=True can sometimes cause double-loading of the model
    # which might crash your RAM (the 10% warning you keep seeing).
    # If it crashes, try setting debug=False.
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True, use_reloader=False)
