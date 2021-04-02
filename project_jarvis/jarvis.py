import pyttsx3
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(f"{day} , {month}, {year}")



def greeting():
    hour = datetime.datetime.now().hour
    if  hour >= 6 and hour <= 10:
        speak("Доброе утро, Сэр!")
    else:
        speak("Добрый день, Сэр!")
    speak("Время сейчас: ")
    speak(time())


greeting()