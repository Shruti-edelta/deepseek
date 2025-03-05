import speech_recognition as sr
import sounddevice as sd
import pyttsx3
import subprocess
import re
import numpy as np


model="deepseek-r1"

engine = pyttsx3.init()
mode=True
def speak(cleaned_output):
    engine.setProperty('rate', 150)
    if mode:
        print("======***")
        engine.say(cleaned_output)
        engine.runAndWait()
    else:
        engine.stop()

def listen():
    print("speech")
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  #voice handle with threshod value(noise)
        print("Please say something:")
        audio = recognizer.listen(source)
        try:
            g_text = recognizer.recognize_google(audio)
            print("=====",g_text)
            return g_text
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said")
            return None
        except sr.RequestError as e:
            print("Error; {0}".format(e))
            return None
        
def auto_answer(text):
    r=subprocess.run(['ollama','run',model,text],capture_output=True,text=True)
    cleaned_output = re.sub(r'<.*?>','',r.stdout)
    cleaned_output=cleaned_output.replace('**', ' ')
    return cleaned_output

while True:
    print("in")
    text=listen()
    
    if text.upper()=="BREAK": 
        print("=====")
        break
    else:
        speak(auto_answer(text))




def check_for_sound(indata):
    """Function to check if sound (or speech) is detected by calculating the volume."""
    # Calculate the volume (magnitude) of the audio data
    volume_norm = np.linalg.norm(indata) * 10  # Increase the multiplier for sensitivity
    
    if volume_norm > 500:
        return True
    else:
        return False

def audio_callback(indata, frames, time, status):
    """Callback function to process the audio data and detect sound."""
    if status:
        print(status, flush=True)
    
    # Check if sound is detected based on the volume
    if check_for_sound(indata):
        print("Sound detected!")
        speak("Sound detected!")  # Respond via TTS
    else:
        print("No sound detected.")

# if user_input == 'exit':
#             break
#         elif user_input == 'pause':
#             listening = False  # Pause the listening loop
#             speak("Listening paused. Type 'start' to resume.")
#         elif user_input == 'start':
#             listening = True  # Resume listening
#             speak("Resuming listening...")


# recognizer = sr.Recognizer()

# while True:
#     with sr.Microphone() as source:
#         print("Adjusting for ambient noise... Please wait.")
#         recognizer.adjust_for_ambient_noise(source)
#         print("Listening for your speech... Speak now!")
#         try:            
#             audio = recognizer.listen(source)
#             print("Processing your speech...",type(audio))
#             text = recognizer.recognize_google(audio)
#             print("=====",text)
#             if text.upper()=="BREAK":
#                 print("=====")
#                 break
#             else:
#                 engine = pyttsx3.init()
#                 r=subprocess.run(['ollama','run',model,text],capture_output=True,text=True)
#                 engine.setProperty('rate', 150)  
#                 engine.setProperty('volume', 1) 
#                 cleaned_output = re.sub(r'<.*?>','',r.stdout)
#                 cleaned_output=cleaned_output.replace('**', ' ')
#                 print(cleaned_output)
#                 engine.say(cleaned_output)
#                 engine.runAndWait()

#         except sr.UnknownValueError:
#             print("Sorry, I could not understand what you said.")
#         except sr.RequestError as e:
#             print(f"Could not request results from Google Speech Recognition service; {e}")

