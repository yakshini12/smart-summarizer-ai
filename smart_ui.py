import os
os.environ["PYTORCH_JIT"] = "0"

import streamlit as st
import tempfile
import speech_recognition as sr

from summarizer import summarize_text
from pdf_summarizer import extract_text_from_pdf
from audio_transcriber import transcribe_audio
from yt_summarizer import download_audio_from_youtube
from tts_speaker import speak_summary

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Smart Summarizer", layout="centered")
st.title("🧠 Smart Summarizer AI")
st.subheader("Summarize Text, PDFs, Audio, YouTube, or Mic Input — with Voice Output")

# --- Input Mode Selection ---
input_type = st.radio("Choose input type:", ["Text", "PDF", "Audio File", "YouTube Link", "Mic Input"])

summary = ""

# --- Text Input ---
if input_type == "Text":
    user_text = st.text_area("Enter or paste your text:", height=200)
    if st.button("Summarize"):
        if user_text.strip():
            summary = summarize_text(user_text)
        else:
            st.warning("⚠️ Please enter some text.")

# --- PDF Upload ---
elif input_type == "PDF":
    uploaded_pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_pdf and st.button("Summarize"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_pdf.read())
            pdf_text = extract_text_from_pdf(tmp.name)
        summary = summarize_text(pdf_text)

# --- Audio File Upload ---
elif input_type == "Audio File":
    uploaded_audio = st.file_uploader("Upload an audio file (MP3 or WAV)", type=["mp3", "wav"])
    if uploaded_audio and st.button("Summarize"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tmp.write(uploaded_audio.read())
            transcript = transcribe_audio(tmp.name)
        summary = summarize_text(transcript)

# --- YouTube Link ---
elif input_type == "YouTube Link":
    yt_url = st.text_input("Paste the YouTube video URL here")
    if yt_url and st.button("Summarize"):
        try:
            output_file = "yt_temp_audio.mp3"
            download_audio_from_youtube(yt_url, output_file)
            transcript = transcribe_audio(output_file)
            summary = summarize_text(transcript)
            os.remove(output_file)
        except Exception as e:
            st.error(f"❌ Failed to process video: {e}")

# --- Mic Input (Speech-to-Text) ---
elif input_type == "Mic Input":
    def record_and_transcribe():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎧 Listening... Speak now.")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            st.info("🔄 Transcribing your voice...")
            return r.recognize_google(audio)
        except sr.UnknownValueError:
            return "❌ Could not understand the audio."
        except sr.RequestError as e:
            return f"❌ API error: {e}"

    if st.button("🎧 Record and Summarize"):
        transcript = record_and_transcribe()
        st.markdown("### 📝 You said:")
        st.write(transcript)

        if "❌" not in transcript:
            summary = summarize_text(transcript)

# --- Display Summary + Options ---
if summary:
    st.markdown("### 📌 Summary:")
    st.write(summary)

    if st.button("🔊 Speak Summary"):
        speak_summary(summary)

    st.download_button(
        label="📎 Download Summary",
        data=summary,
        file_name="summary.txt",
        mime="text/plain"
    )
