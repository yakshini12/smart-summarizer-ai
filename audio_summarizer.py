print("📦 Using summarizer from:", __file__)
from audio_transcriber import transcribe_audio
from summarizer import summarize_text # Reuse your existing function

# Path to your fixed audio file
audio_path = "test_audio.mp3"

# Transcribe
transcript = transcribe_audio(audio_path)
print("\n📝 Transcript Preview:\n", transcript[:500])

# Summarize
summary = summarize_text(transcript, num_sentences=3)
print("\n📌 Summary:\n", summary)
from tts_speaker import speak_summary

choice = input("\n🎧 Want to hear the summary? (y/n): ").lower()
if choice == 'y':
    speak_summary(summary)
