import pyttsx3

def speak_summary(summary_text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Try voices[0] if this fails

    print("\n🔊 Speaking the summary...\n")
    engine.say(summary_text)
    engine.runAndWait()
