[![Twitter: @NorowaretaGemu](https://img.shields.io/badge/X-@NorowaretaGemu-blue.svg?style=flat)](https://x.com/NorowaretaGemu)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<br>
<div align="center">
  <a href="https://ko-fi.com/cursedentertainment">
    <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi" style="width: 20%;"/>
  </a>
</div>
<br>

<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/python%20-%23323330.svg?&style=for-the-badge&logo=python&logoColor=white"/>
</div>

<div align="center">
    <img alt="TensorFlow" src="https://img.shields.io/badge/tensorflow%20-%23323330.svg?&style=for-the-badge&logo=tensorflow&logoColor=white"/>
    <img alt="Flask" src="https://img.shields.io/badge/flask%20-%23323330.svg?&style=for-the-badge&logo=flask&logoColor=white"/>
</div>

# CursedGPT

<div align="center">
<a href="https://cursedprograms.github.io/cursedgpt-pr/" target="_blank">
    <img src="https://github.com/CursedPrograms/Cursed-GPT/raw/main/demo_images/cover.png"
        alt="CursedGPT">
</a>
</div>
<br>

```bash
"you suck, but you're not going to do anything about it."
```
CursedGPT leverages the Hugging Face Transformers library to interact with a pre-trained GPT-2 model. It employs TensorFlow for model management and AutoTokenizer for efficient tokenization. The script enables users to input prompts interactively, generating text responses from the GPT-2 model. To improve the user experience, unnecessary warning messages related to the transformers library are effectively suppressed.

## Scripts:

- **main.py:** The selection menu for CursedGPT
- **app.py:** Run CursedGPT as a web-server

### /scripts/

- **transformer.py:** Run CursedGPT
- **transformer_t2s.py:** Run CursedGPT with text-to-speech functionality
- **transformer_s2t2s.py:** Run CursedGPT with speech-to-text-to-speech functionality
- **transformer_webcam.py:** Run CursedGPT with webcam functionality
- **install_dependencies.py:** Install dependencies

### /scripts/system

- **generate_text.py:** The GPT text generator
- **clean_text.py:** Clean text from recorded voice audio
- **stt.py:** Speech-to-text
- **tts.py:** Text-to-speech
- **capture_photo.py:** Capture photo with a webcam
- **play_audio.py:** Play generated audio

## How to Run:

### Environment Setup/Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
```bash
pip install torch torchvision torchaudio
```
### Run main.py for terminal interactivity

```bash
python main.py
```
### Run app.py for flask web server

```bash
python app.py
```

## Requirements:

```bash
Package                  Version
------------------------ ----------
absl-py                  2.4.0
astunparse               1.6.3
beautifulsoup4           4.10.0
blinker                  1.9.0
certifi                  2026.2.25
charset-normalizer       3.4.7
click                    8.1.8
filelock                 3.25.2
Flask                    3.0.0
flatbuffers              25.12.19
fsspec                   2026.3.0
gast                     0.7.0
google-pasta             0.2.0
grpcio                   1.80.0
gTTS                     2.5.0
h5py                     3.14.0
hf-xet                   1.4.3
huggingface_hub          0.36.2
idna                     3.11
itsdangerous             2.2.0
Jinja2                   3.1.6
keras                    3.14.0
libclang                 18.1.1
markdown-it-py           4.0.0
MarkupSafe               3.0.3
mdurl                    0.1.2
ml_dtypes                0.5.4
mpmath                   1.3.0
namex                    0.1.0
networkx                 3.6.1
numpy                    2.4.4
nvidia-cublas-cu12       12.1.3.1
nvidia-cuda-cupti-cu12   12.1.105
nvidia-cuda-nvrtc-cu12   12.1.105
nvidia-cuda-runtime-cu12 12.1.105
nvidia-cudnn-cu12        8.9.2.26
nvidia-cufft-cu12        11.0.2.54
nvidia-curand-cu12       10.3.2.106
nvidia-cusolver-cu12     11.4.5.107
nvidia-cusparse-cu12     12.1.0.106
nvidia-nccl-cu12         2.20.5
nvidia-nvjitlink-cu12    12.9.86
nvidia-nvtx-cu12         12.1.105
opt_einsum               3.4.0
optree                   0.19.0
packaging                26.0
pillow                   12.2.0
pip                      24.0
protobuf                 7.34.1
PyAudio                  0.2.14
pydub                    0.25.1
pygame                   2.5.2
Pygments                 2.20.0
pyttsx3                  2.99
PyYAML                   6.0.3
regex                    2026.3.32
requests                 2.33.1
rich                     14.3.3
safetensors              0.7.0
setuptools               82.0.1
six                      1.17.0
soupsieve                2.8.3
SpeechRecognition        3.10.1
sympy                    1.14.0
tensorflow               2.21.0
termcolor                3.3.0
tf_keras                 2.21.0
tokenizers               0.15.2
torch                    2.3.1
torchaudio               2.3.1
torchvision              0.18.1
tqdm                     4.67.3
transformers             4.37.1
typing_extensions        4.15.0
urllib3                  2.6.3
Werkzeug                 3.1.8
wheel                    0.46.3
wrapt                    2.1.2
```

<br>

<div align="center">
<a href="https://synthwomb-synthia.onrender.com/" target="_blank">
    <img src="https://github.com/SynthWomb/Synthia/raw/main/demo_images/synthia00-cover.png"
        alt="SynthiaGPT">
</a>
</div>
<br>

- [GloriosaAI Repository](https://github.com/CursedPrograms/GloriosaAI)
- [Gender-Age-ID Repository](https://github.com/CursedPrograms/Gender-Age-ID)
- [Detect-Face Repository](https://github.com/CursedPrograms/Detect-Face)
- [Image-Generator Repository](https://github.com/CursedPrograms/Image-Generator)

<br>
<div align="center">
<a href="https://github.com/SynthWomb" target="_blank" align="center">
    <img src="https://github.com/SynthWomb/synth.womb/blob/main/logos/synthwomb07.png"
        alt="SynthWomb" style="width:200px;"/>
</a>
</div>
<br>
<div align="center">
<a href="https://cursed-entertainment.itch.io/" target="_blank">
    <img src="https://github.com/CursedPrograms/cursedentertainment/raw/main/images/logos/logo-wide-grey.png"
        alt="CursedEntertainment Logo" style="width:250px;">
</a>
</div>
