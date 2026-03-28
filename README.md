# 🎵 OCR to Speech Converter

> **Transform images into spoken audio instantly!**  
> A powerful, multilingual tool that extracts text from images and reads it aloud with high-quality speech synthesis.

---

## 📸 Project Showcase

| 📥 Upload Image | 📝 Extracted Text | 🔊 Audio Output |
| :--- | :--- | :--- |
| ![Upload](screenshots/upload_image.png) | ![Text](screenshots/extracted_text.png) | ![Audio](screenshots/audio_output.png) |

---

## ✨ Key Features

- **🔍 High Precision OCR**: Leveraging **Tesseract OCR** for accurate text extraction.
- **🔊 Natural Speech Synthesis**: Powered by **gTTS** for crisp, clear audio generation.
- **🌐 Multilingual Support**: 
  - 🇮🇳 Tamil
  - 🇮🇳 Hindi
  - 🇺🇸 English
  - 🇫🇷 French
  - 🇪🇸 Spanish
- **⬇️ Instant Download**: Save your generated audio as `.mp3` for offline use.
- **🖥️ Sleek Interface**: A clean, intuitive **Streamlit** dashboard.

---

## 🛠️ Tech Stack

- **Core**: `pytesseract` (OCR), `gTTS` (TTS), `Pillow` (Image Processing)
- **UI/UX**: `Streamlit`
- **Logic**: `Python`

---

## 🚀 Getting Started

### 📋 Prerequisites

Ensure you have **Tesseract OCR** installed on your machine:
- **Windows**: [Download Tesseract Installer](https://github.com/UB-Mannheim/tesseract/wiki)
- **Linux**: `sudo apt install tesseract-ocr`
- **Mac**: `brew install tesseract`

### 💻 Local Installation

1. **Clone the repository:**
   ```bash
   git clone http://github.com/kokilamariyayi/ocr-to-sppech.git
   cd ocr-to-sppech
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the app:**
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```bash
ocr-to-speech/
├── app.py                  # Streamlit Web Interface
├── ocr_to_speech.py        # Core Logic (OCR + TTS)
├── requirements.txt        # Python Dependencies
├── screenshots/            # Visual Assets
└── README.md
```

---

## 💡 Use Cases

- **📖 Education**: Convert scanned pages or textbooks into audiobooks.
- **♿ Accessibility**: Assist visually impaired users in reading printed content.
- **🌍 Language Learning**: Practice pronunciation by converting foreign text into audio.
- **📊 Business**: Quickly digitize and listen to printed reports or notes.

---

## 📬 Let's Connect

If you found this project useful, feel free to reach out for collaborations or feedback!

- **LinkedIn**: [Kokila M](https://www.linkedin.com/in/kokila-m-ai-ds/)
- **Email**: [kokilakoki3376@gmail.com](mailto:kokilakoki3376@gmail.com)
- **GitHub**: [kokilamariyayi](https://github.com/kokilamariyayi)

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---
<div align="center">
  <b>Built with ❤️ by Kokila M</b>
</div>
