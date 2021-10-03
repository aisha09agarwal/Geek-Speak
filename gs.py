import speech_recognition as sr
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import pyjokes
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("voice","english")

#saying response
def talk(text):
    engine.say(text)
    engine.runAndWait()

#voice recognition
def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=2)
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            print(command)
    except:
        command = "Not Recognised"

    return command

#command interpretation
def run_geekspeak():
    command = take_command()
    print(command)

    if "play" in command:
        song = command.replace("play"," ")
        talk("Playing"+song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk(time)

    elif "who is" in command:
        person = command.replace("who is","")
        info =wikipedia.summary(person,1)
        print(info)
        talk(info)
        
    elif "what is your name" in command:
        print("My name is Alexa")
        talk("My name is Alexa")

    elif "what is" in command:
        object = command.replace("what is","")
        info = wikipedia.summary(object,1)
        print(info)
        talk(info)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "quit" in command:
        sys.exit()

    else:
        talk("Command not Recognized")

while True:
    run_geekspeak()