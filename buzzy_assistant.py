# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 20:13:23 2021

@author: Raahim
"""
import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk('My name is Buzzy and How can I help you Sir')
            voice = listener.listen(source) #use mic as as source and listener to listen!
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'buzzy' in command:
                command = command.replace('buzzy','')
                #print(command)
    except:
        pass
    return command


def run():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play',' ')
        talk('playing'+song)
        pywhatkit.playonyt(song)
        print('playing'+ song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I : %M %p')
        talk('Now it is' + time)
    elif 'search' in command:
        result = command.replace('search','')
        info = wikipedia.summary(result, 1)
        talk(info)
    elif 'do you know me' in command:
        talk('You are my boss! You are handsome! Your wife is a mad')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say again sir!')
    
while(1):
    run()