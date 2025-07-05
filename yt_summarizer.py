import os
import subprocess
from audio_transcriber import transcribe_audio
from summarizer import summarize_text
from tts_speaker import speak_summary

def download_audio_from_youtube(url, output_file="yt_audio.mp3"):
    print("⬇️ Downloading YouTube audio...")
    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", output_file,
        url
    ]
    subprocess.run(command, check=True)
    return output_file

if __name__ == "__main__":
    yt_url = input("🎥 Enter YouTube video URL: ").strip()
    audio_file = "yt_audio.mp3"

    try:
        download_audio_from_youtube(yt_url, audio_file)

        transcript = transcribe_audio(audio_file)
        print("\n📝 Transcript Preview:\n", transcript[:500])

        summary = summarize_text(transcript, num_sentences=3)
        print("\n📌 Summary:\n", summary)

        choice = input("\n🎧 Want to hear the summary? (y/n): ").lower()
        if choice == 'y':
            speak_summary(summary)

    except Exception as e:
        print("❌ Error:", e)
