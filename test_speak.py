import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print("🔊 Trying to speak...")
engine.say("This is a test summary. Hello Yakshini!")
engine.runAndWait()
print("✅ Done.")
