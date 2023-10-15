# Imports
import pyttsx3

# Initializes TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'en-us')
engine.setProperty('voice', voices[0].id)


def TextToWAV(text, output_path, rate = 300):
    # Sets voice speed
    engine.setProperty('rate', rate) # 300 = highest rate
    # Saves as WAV
    engine.save_to_file(text, output_path)
    engine.runAndWait() 

