import pytesseract
from PIL import Image
from gtts import gTTS
import os
import sys

def extract_text_from_image(image_path):
    """Extract text from image using Tesseract OCR."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

def text_to_audio(text, output_file="output.mp3", lang="en"):
    """Convert extracted text to audio using gTTS."""
    if not text:
        print("No text found in image.")
        return
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)
    print(f"Audio saved as: {output_file}")

def image_to_audio(image_path, output_file="output.mp3", lang="en"):
    """Full pipeline: image -> OCR -> audio."""
    print(f"Processing: {image_path}")
    text = extract_text_from_image(image_path)
    print(f"\nExtracted Text:\n{'-'*30}\n{text}\n{'-'*30}")
    text_to_audio(text, output_file, lang)

if __name__ == "__main__":
    image_path = sys.argv[1] if len(sys.argv) > 1 else "sample.png"
    image_to_audio(image_path)
