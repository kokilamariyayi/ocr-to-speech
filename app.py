import streamlit as st
import pytesseract
from PIL import Image
from gtts import gTTS
import os

st.set_page_config(page_title="OCR to Speech", page_icon="🎵", layout="centered")

st.title("🎵 OCR to Speech Converter")
st.markdown("Upload an image containing text — it will be **extracted and read aloud** for you.")
st.divider()

# Language selector
lang_map = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es"
}
lang_choice = st.selectbox("🌐 Select Output Language", list(lang_map.keys()))

# File uploader
uploaded_file = st.file_uploader("📤 Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(img, caption="Uploaded Image", use_column_width=True)

    with col2:
        with st.spinner("Extracting text..."):
            text = pytesseract.image_to_string(img).strip()

        st.subheader("📝 Extracted Text")
        if text:
            st.text_area("", text, height=200)
        else:
            st.warning("No text detected in this image.")

    st.divider()

    if text:
        if st.button("🔊 Convert to Audio", use_container_width=True):
            with st.spinner("Generating audio..."):
                tts = gTTS(text=text, lang=lang_map[lang_choice], slow=False)
                tts.save("output.mp3")

            st.success("✅ Audio generated successfully!")
            st.audio("output.mp3")

            with open("output.mp3", "rb") as f:
                st.download_button(
                    label="⬇️ Download Audio",
                    data=f,
                    file_name="ocr_output.mp3",
                    mime="audio/mpeg",
                    use_container_width=True
                )

st.divider()
st.caption("Built by [Kokila M](https://github.com/kokilamariyayi) | Powered by Tesseract OCR + gTTS")
