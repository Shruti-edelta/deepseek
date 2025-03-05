import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

msg=input("enter message: ")
# Say something
engine.say(msg)

# Wait until speech is finished
engine.runAndWait()