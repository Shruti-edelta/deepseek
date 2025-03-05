import speech_recognition as sr
import sounddevice as sd
import numpy as np


recognizer = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait.")
    recognizer.adjust_for_ambient_noise(source)     #voice handle with threshod value
    print("Listening for your speech... Speak now!")
    try:
        # Capture the speech from the microphone
        audio = recognizer.listen(source)
        print("Processing your speech...")

        # Use Google's speech recognition to convert audio to text
        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
