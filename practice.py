import speech_recognition as sr

def detect_sound():
    recognizer = sr.Recognizer()

    # Using the microphone as the audio source
    with sr.Microphone() as source:
        print("Listening for sound... Please speak.")
        
        # Adjusting for ambient noise (background noise)
        recognizer.adjust_for_ambient_noise(source)
        
        try:
            # Listen for the first sound/input
            audio = recognizer.listen(source, timeout=5)  # Timeout after 5 seconds

            # If sound is detected, print that sound was captured
            print("Sound detected!")
            
            try:
                # Try to recognize speech (if any)
                print("Recognizing speech...")
                text = recognizer.recognize_google(audio)
                print(f"Recognized speech: {text}")
            except sr.UnknownValueError:
                print("Could not understand the audio")
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service")

        except sr.WaitTimeoutError:
            # This is triggered if no sound is detected within the timeout period
            print("No sound detected within the given time.")

# Continuously check for sound
detect_sound()
