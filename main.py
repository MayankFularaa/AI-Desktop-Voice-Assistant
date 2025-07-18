import datetime
import os
import sys
import time
import webbrowser
import pyautogui
import pyttsx3
import speech_recognition as sr
import psutil
# from elevenlabs import generate,play
# from elevenlabs import set_api_key
# set_api_key(api_key_data)

# def engine_talk(query):
#     audio=generate(
#         text=query,
#         voice='Grace',
#         model="eleven_monolingual_v1"
#     )
#     play(audio)



import json
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np

with open("intents.json") as file:
    data=json.load(file)

model=load_model('chat_model.h5')

with open('tokenizer.pkl','rb') as f:
    tokenizer=pickle.load(f)

with open('label_encoder.pkl','rb') as encoder_file:
    label_encoder=pickle.load(encoder_file)



def initialize_engine():
    engine=pyttsx3.init("sapi5")
    voices=engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    rate=engine.getProperty("rate")
    engine.setProperty('rate',rate-20)
    volume=engine.getProperty('volume')
    engine.setProperty('volume',volume+0.50)
    return engine

def speak(test):
    engine=initialize_engine()
    engine.say(test)
    engine.runAndWait()

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        print("Listening.......", end="",flush=True)
        r.phrase_threshold=0.3
        r.pause_threshold=1.0
        r.sample_rate=48000
        r.dynamic_energy_threshold=True
        r.operation_timeout=5
        r.non_speaking_duration=0.5
        r.dynamic_energy_adjustment=2
        r.energy_threshold=4000
        r.phrase_time_limit=10
        print(sr.Microphone.list_microphone_names())
        audio=r.listen(source)

    try:
        print("\n",end="",flush=True)
        print("Recognizing...")
        query=r.recognize_google(audio,laguage='en-in')
        print("\n",end="",flush=True)
        print(f"user said : {query}\n")
    except Exception as e:
        print("Say again Please....")
        return "None"
    return query

def cal_day():
    day=datetime.datetime.today().weekday()+1
    day_dict={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }

    if day in day_dict.keys():
        day_of_week=day_dict[day]
        print(day_of_week)
    return day_of_week


def wishMe():
    hour=int(datetime.datetime.now().hour)
    t=time.strftime("%I:%M:%p")
    day=cal_day()

    if(hour>=0) and (hour<=12) and ("AM" in t):
        speak(f"Good Morning Bose, it's {day} and the time is {t}")
    elif(hour>=12) and (hour<=16) and ("PM" in t):
        speak(f"Good Afternoon Bose, it's {day} and the time is {t}")
    else:
        speak(f"Good Evening Bose, it's {day} and the time is {t}")


def social_media(command):
    if 'facebook' in command:
        speak("Opening your facebook")
        webbrowser.open("https://www.facebook.com/")

    elif 'whatsapp' in command:
        speak("Opening your whatsapp")
        webbrowser.open("https://web.whatsapp.com/")

    elif 'discord' in command:
        speak("Opening your Discord")
        webbrowser.open("https://discord.com/")

    elif 'Linkedin' in command:
        speak("Opening your Linkedin")
        webbrowser.open("https://www.linkedin.com/")

    elif 'instagram' in command:
        speak("Opening your instagram")
        webbrowser.open("https://www.instagram.com/")

    else:
        speak("No Result Found")


def schedule():
    day=cal_day().lower()
    speak("Bose today's schedule is ")
    week={
        'monday':"Boss,from 9:00 am to 9:50 am you have algorithm class and form 9:50 am to 10:40 you have data science class then 10:40 am to 11:00 am you have small tree break then from 11:00 am to 11:50am you have machine learning class",
        'tuesday':"Boss,from 9:00 am to 9:50 am you have Statistics class and form 9:50 am to 10:40 you have deployment class then 10:40 am to 11:00 am you have small tree break then from 11:00 am to 11:50am you have Deep Learning class",
        'wednesday':"Boss,from 9:00 am to 9:50 am you have algorithm class and form 9:50 am to 10:40 you have data science class then 10:40 am to 11:00 am you have small tree break then from 11:00 am to 11:50am you have machine learning class",
        'thursday':"Boss,from 9:00 am to 9:50 am you have statistics class and form 9:50 am to 10:40 you have deployment class then 10:40 am to 11:00 am you have small tree break then from 11:00 am to 11:50am you have deep learning class",
        'friday':"Boss,from 9:00 am to 9:50 am you have NLP class and form 9:50 am to 10:40 you have data science class then 10:40 am to 11:00 am you have small tree break then from 11:00 am to 11:50am you have machine learning class",
        'saturday':"Boss,Today you have only one class that is Major Project Class",
        'sunday':"Boss,Today is the Fun day"
    }

    if day in week.keys():
        speak(week[day])


def openApp(command):
    if "calculator" in command:
        speak("Opening calculator")
        os.startfile("C:\\Windows\\System32\\calc.exe")
    
    if "notepad" in command:
        speak("Opening notepad")
        os.startfile("C:\\Windows\\System32\\notepad.exe")

    if "paint" in command:
        speak("Opening paint")
        os.startfile("C:\\Windows\\System32\\mspaint.exe")

def closeApp(command):
    if "calculator" in command:
        speak("closing calculator")
        os.system("taskkill /f /im calc.exe")
    
    if "notepad" in command:
        speak("closing notepad")
        os.system("taskkill /f /im notepad.exe")

    if "paint" in command:
        speak("closing paint")
        os.system("taskkill /f /im mspaint.exe")

def browsing(query):
    if 'google' in query or 'browser' in query:
        speak("Boss, what should I search on Google?")
        #s = command().lower()
        s=input("What should i search on google")
        
        webbrowser.open(f"https://www.google.com/search?q={s}")


def condition():
    usage=(psutil.cpu_percent())
    speak("CPU is at {usage} percentage")
    battery=psutil.sensors_battery()
    percentage=battery.percent
    speak('Boss our system have {percentage} percentage battery')

    if percentage>=80:
        speak("Boss we could have enough charging to continue our work")
    elif percentage>=40 and percentage<=75:
        speak("boss we should connect our system to charging point to charge battery")
    else:
        speak("Boss we have very low power please connect the charger")



if __name__=="__main__":
    #wishMe()
    engine_talk("allow me to introduce myself I am mayank , the virtual artificial Intelligence and i am here to assist you with the variety of tasks as best as i can , what can i help you.")
    while True:
        query=command().lower()
        #query=input("Enter Your command -> ")
        if('facebook' in query) or ('discord' in query) or ('linkedin' in query) or ('instagram' in query) or ('whatsapp' in query):
            social_media(query)
        
        elif("university time table" in query) or ("schedule" in query):
            schedule()

        elif("volume up" in query) or ("increase volume" in query):
            pyautogui.press("volumeup")
            speak("Volume increased")

        elif("volume down" in query) or ("decrease volume" in query):
            pyautogui.press("volumedown")
            speak("Volume decreased")

        elif("mute" in query) or ("mute the sound" in query):
            pyautogui.press("volumemute")
            speak("volume muted")
        
        elif("unmute" in query) or ("unmute the sound" in query):
            pyautogui.press("volumeunmute")
            speak("volume unmuted")
        
        elif("open calculator" in query) or ("open notepad" in query) or ("open paint" in query):
            openApp(query)

        elif("close calculator" in query) or ("close notepad" in query) or ("close paint" in query):
            closeApp(query)

        elif('what' in query) or ('who' in query) or ('how' in query) or ('hi' in query) or ('thanks' in query) or ('hello' in query):
            padded_sequences=pad_sequences(tokenizer.texts_to_sequences([query]),maxlen=20,truncating='post')
            result=model.predict(padded_sequences)
            tag=label_encoder.inverse_transform([np.argmax(result)])

            for i in data['intents']:
                if i['tag']==tag:
                    speak(np.random.choice(i['responses']))

        elif('open google' in query) or ("open browser" in query):
            browsing(query)

        elif('system condition' in query) or ('condition of system' in query):
            speak("checking the system condition")
            condition()

        elif "exit" in query:
            sys.exit()
    #     print(query)
#speak("Hello, i'm Mohini")