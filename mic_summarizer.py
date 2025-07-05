import speech_recognition as sr
from summarizer import summarize_text
from tts_speaker import speak_summary

def record_and_transcribe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now... (listening)")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    print("🔄 Transcribing...")
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "❌ Could not understand audio."
    except sr.RequestError as e:
        return f"API error: {e}"

if __name__ == "__main__":
    transcript = record_and_transcribe()
    print("\n📝 You said:\n", transcript)

    if "❌" not in transcript:
        summary = summarize_text(transcript, num_sentences=2)
        print("\n📌 Summary:\n", summary)

        choice = input("\n🎧 Want to hear the summary? (y/n): ").lower()
        if choice == 'y':
            speak_summary(summary)
