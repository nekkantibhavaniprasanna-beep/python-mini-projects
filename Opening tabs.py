import speech_recognition as sr
import sounddevice as sd
import soundfile as sf
import pyttsx3
import subprocess
engine = pyttsx3.init()
r=sr.Recognizer()
fs=16000
while True:
    print("Speak...")
    recording=sd.rec(int(5*fs),samplerate=fs,channels=1)
    sd.wait()
    sf.write("output.wav",recording,fs)
    with sr.AudioFile("output.wav") as source:
        audio=r.record(source)
    try:
        text=r.recognize_google(audio).lower()
        print("You said: " + text)

        if "notepad" in text:
            engine.say("Opening Notepad")
            engine.runAndWait()
            subprocess.Popen('notepad.exe')

        elif "calculator" in text:
            engine.say("Opening Calculator")
            engine.runAndWait()
            subprocess.Popen('calc.exe')

        elif "paint" in text:
            engine.say("Opening Paint")
            engine.runAndWait()
            subprocess.Popen('mspaint.exe')
        elif "youtube" in text:
            engine.say("Opening YouTube")
            engine.runAndWait()
            subprocess.Popen('start https://www.youtube.com', shell=True)
        elif "google" in text:
            engine.say("Opening Google")
            engine.runAndWait()
            subprocess.Popen('start https://www.google.com', shell=True)

        elif "exit" in text:
            engine.say("Exiting the program")
            engine.runAndWait()
            break
        else:
            engine.say("Command not recognized. Please try again.")
            engine.runAndWait()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        