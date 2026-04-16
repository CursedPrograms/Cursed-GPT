[![Twitter: @NorowaretaGemu](https://img.shields.io/badge/X-@NorowaretaGemu-blue.svg?style=flat)](https://x.com/NorowaretaGemu)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<div align="center">
  <a href="https://ko-fi.com/cursedentertainment">
    <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ko-fi" style="width: 20%;"/>
  </a>
</div>
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

---

```bash
"you suck, but you're not going to do anything about it."
```

---

## 📖 Overview

<details>
<summary><b>Overview</b></summary>

CursedGPT leverages the Hugging Face Transformers library to interact with a pre-trained GPT-2 model. It employs TensorFlow for model management and AutoTokenizer for efficient tokenization. The script enables users to input prompts interactively, generating text responses from the GPT-2 model. To improve the user experience, unnecessary warning messages related to the transformers library are effectively suppressed.

</details>

---

## Scripts

<details>
<summary><b>Scripts</b></summary>

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

</details>

---

## How to Run:

### Environment Setup

<details>
<summary><b>Environment Setup</b></summary>

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
```bash
pip install torch torchvision torchaudio
```

</details>

### Run main.py for terminal interactivity

```bash
python main.py
```
### Run app.py for flask web server

```bash
python app.py
```

---

<div align="center">
<a href="https://synthwomb-synthia.onrender.com/" target="_blank">
    <img src="https://github.com/SynthWomb/Synthia/raw/main/demo_images/synthia00-cover.png"
        alt="SynthiaGPT">
</a>
</div>

---

## Related Projects

- [GloriosaAI](https://github.com/CursedPrograms/GloriosaAI)
- [Gender-Age-ID](https://github.com/CursedPrograms/Gender-Age-ID)
- [Detect-Face](https://github.com/CursedPrograms/Detect-Face)
- [Image-Generator](https://github.com/CursedPrograms/Image-Generator)

---

<br>
<div align="center">
<a href="https://github.com/SynthWomb" target="_blank" align="center">
    <img src="https://github.com/SynthWomb/synth.womb/blob/main/logos/synthwomb07.png"
        alt="SynthWomb" style="width:200px;"/>
</a>
</div>
<br>
<div align="center">
© Cursed Entertainment 2026
</div>
<br>
<div align="center">
<a href="https://cursed-entertainment.itch.io/" target="_blank">
    <img src="https://github.com/CursedPrograms/cursedentertainment/raw/main/images/logos/logo-wide-grey.png"
        alt="CursedEntertainment Logo" style="width:250px;">
</a>
</div>
