import speech_recognition as sr
from gtts import gTTS
import playsound
from datetime import datetime
from pynput.keyboard import Key, Controller
import time
from tkinter import *

root = Tk()
root.geometry("500x300")

myLabel = Label(root, text="Listening")
myLabel.pack()

root.mainloop()

keyboard = Controller()

def speak(text):
    tts = gTTS(text=text, lang="en")
    date_string = datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception" + str(e))

    return said


text = get_audio()
if "chat" in text:
    speak("Listening")
    chat = get_audio()





    keyboard.press(Key.enter)
    time.sleep(1)
    for letter in chat:
        keyboard.type(letter)
        time.sleep(0.1)
    keyboard.press(Key.enter)