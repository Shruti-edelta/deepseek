import os
from gtts import gTTS

# Hindi text
t = "hello"

# Convert Hindi text to speech
tts = gTTS(t, lang='hi')

# Save the audio to a file
tts.save("hindi_audio.mp3")

# Play the audio (macOS)
os.system("afplay hindi_audio.mp3")  # macOS

