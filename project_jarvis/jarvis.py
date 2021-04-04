import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import psutil
import webbrowser as wb
import smtplib
import pyautogui
import os

engine = pyttsx3.init()
engine.setProperty('rate', 178)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
listener = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)


def greetings():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning, Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon, Sir!")
    elif hour >= 18 and hour < 24:
        speak("Good evening, Sir!")
    else:
        speak("Good night, Sir!")
    time()
    speak("Jarvis at your service. Please tell me how can i help you?")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nurkamal433@gmail.com', 'ZXC123Asd')
    server.sendmail('nurkamal433@gmail.com', to, content)
    server.close()


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at ' + usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as audio_source:
        speak("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(audio_source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    greetings()
while True:
    query = take_command().lower()
    if 'time' in query:
        time()
    elif 'play' in query:
        song = query.replace('play', '')
        speak("Playing " + song)
        pywhatkit.playonyt(song)
    elif 'who the heck is' in query:
        person = query.replace('who the heck is', '')
        speak(wikipedia.summary(person, 1))
    elif 'send email' in query:
        try:
            speak("What should i sent?")
            content = take_command()
            to = 'nurkamal433@gmail.com'
            sendEmail(to, content)
            speak('Email has been sent!')
        except Exception as e:
            print(e)
            speak('Sorry, sir! I cannot send the email')

    elif 'search' in query:
        speak('What info do you need?')

        # If your chrome app is located in other dir, change chromepath variable to it
        chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        search = take_command().lower()
        wb.get(chromepath).open_new_tab(search + '.com')

    elif 'shutdown' in query:
        os.system("shutdown /s /t 1")

    elif 'restart' in query:
        os.system("shutdown /r /t 1")
    elif 'cpu' in query:
        cpu()
