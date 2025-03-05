import sounddevice as sd
import numpy as np
import time

# Parameters
RATE = 4000  # Sample rate (samples per second)
BLOCKSIZE = 1024  # Number of frames per buffer (instead of frames_per_buffer)
THRESHOLD = 20  # Volume threshold to detect sound (adjust as needed)

def check_for_sound(indata):
    """Check if sound is detected based on the volume of the audio data."""
    # Calculate the volume (magnitude) of the audio data
    volume_norm = np.linalg.norm(indata) * 10  # Increase the multiplier for sensitivity
    
    if volume_norm > THRESHOLD:
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
    else:
        print("No sound detected.")

def main():
    """Main function to continuously check for sound detection."""
    with sd.InputStream(callback=audio_callback, samplerate=RATE, blocksize=BLOCKSIZE):
        print("Listening for sound... Press Ctrl+C to stop.")
        while True:
            time.sleep(0.7)  # Keep the program running and checking for sound

if __name__ == "__main__":
    main()
