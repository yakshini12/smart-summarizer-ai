# 🧠 Smart Summarizer AI

**An offline, AI-powered app that summarizes:**
- 📝 Text
- 📄 PDFs
- 🎧 Audio files (MP3/WAV)
- 📽️ YouTube videos
- 🎙️ Mic input

With voice output 🎤 and NO internet or API required.

---

## 🚀 Features

✅ Extractive summarization using **TF-IDF + TextRank**  
✅ Transcription using **Whisper (offline)**  
✅ Auto-trim **YouTube audio to 60s** for fast summaries  
✅ 🎧 Voice summary via `pyttsx3`  
✅ No OpenAI key or API dependency  
✅ Built with **Python + Streamlit**  
✅ Free, fast, and accessible — for everyone

---

## 🌟 Tech Stack

| Module              | Description                          |
|---------------------|--------------------------------------|
| `Streamlit`         | Web app interface                    |
| `nltk`, `sklearn`   | Text processing + summarization      |
| `openai-whisper`    | Offline transcription                |
| `pytube`, `pydub`   | YouTube download + audio trimming    |
| `speech_recognition`| Voice-to-text from mic input         |
| `pyttsx3`           | Offline text-to-speech               |
| `PyMuPDF`           | PDF text extraction                  |

---

## 📂 Project Structure

smart_summarize_pro/
├── smart_ui.py              # 🎛️ Streamlit user interface (main app)
├── summarizer.py            # 🧠 Extractive summarization using TF-IDF + TextRank
├── audio_transcriber.py     # 🎧 Transcribe audio using Whisper
├── pdf_summarizer.py        # 📄 Extract text from PDF files
├── yt_summarizer.py         # 📽️ Download and trim YouTube audio
├── tts_speaker.py           # 🔊 Convert summary to speech (TTS)
├── requirements.txt         # 📦 Python dependencies
└── README.md                # 📘 Project documentation

---

## 🔧 How to Run Locally

```bash
git clone https://github.com/yakshini12/smart-summarizer-ai.git
cd smart-summarizer-ai
pip install -r requirements.txt
streamlit run smart_ui.py

Then open http://localhost:8501 in your browser 🌐

🧪 Input Types Supported

| Input Mode   | Description                        |
| ------------ | ---------------------------------- |
| Text         | Paste plain text                   |
| PDF          | Upload `.pdf` file                 |
| Audio File   | Upload `.mp3` or `.wav`            |
| YouTube Link | Paste a video link (auto-trimmed)  |
| Mic Input    | Speak live through your microphone |

💾 Voice Output
Click the "🔊 Speak Summary" button to hear the AI read the summary aloud using pyttsx3.

🙌 Made with Love by
👩‍💻 Patila Yakshini

“Bringing AI to everyone — offline, free, and accessible.”

📌 License
This project is open-source and free to use for learning, demos, or community support.
