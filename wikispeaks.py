import speech_recognition as s
import pyttsx3
import wikipedia
import pyaudio

def Input():
    reco = s.Recognizer()
    with s.Microphone() as source:
        print("Please speak what you want to search")
        audio = reco.listen(source)
        query = reco.recognize_google(audio)
    return query

def speak(string):
    e = pyttsx3.init()
    e.say(string)
    e.runAndWait()

def out():
    query = Input().lower()
    print("You said: {query}")
    result = wikipedia.summary(query , sentence = 4)
    print(result)
    speak("Wiki says")
    speak(result)

speak("You need help?")
speak("What do you want to search on wikipedia?")
out()


