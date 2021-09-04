import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui 
import psutil
import pyjokes
#GOOGLE_APPLICATION_CREDENTIALS ="C:\Users\Rajat Sharma\Desktop\python jarvis\jarvis-324212-519a74dd437a.json"

engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) ## 0 is for male. 1 is for female
newVoiceRate = 190 
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#speak("Hello Rajat this line is being read from your python code")

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

#time()    

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def WishMe():
    speak("Welcome to the Python Jarvis")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <=12:
        speak("Good Morning")
    elif hour >12 and hour <= 16:
        speak("Good Afternoon")
    elif hour >16 and hour <=20:
        speak("Good Evening")
    else:
        speak("Good Night")    

    speak("How can I help you")

#date()

#WishMe()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
         print("Recognizing ...")
         query = r.recognize_google(audio)
         print(query)
    except Exception as e:
        print(e)
        speak("Please repeat your statement")

        return "None"

    return query

#TakeCommand()        

def SendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("rejtshawarma@gmail.com", "Rajat@9782")
    server.sendmail("rajatsharmaalt@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\Users\Rajat Sharma\Desktop\python jarvis\ss.png")

def cpu():
    usage = str(psutil.cpu_percent)
    speak("CPU is at " + usage)

    battery = psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":

    WishMe()

    while(True):
        query = TakeCommand().lower()
        print(query)

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "wikipedia" in query:
            speak("Searching your article on Wikipedia")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)

        elif "offline" in query:
            quit() 

        elif "send mail" in query:
            try:
                speak("What message should the mail have ?")   
                content = TakeCommand()
                to = "rajatawesome101@gmail.com"   
                SendMail(to, content)
                speak("Email sent sucessfully")

            except Exception as e:
                speak(e)
                speak("Unable to send the message")

        elif "search in chrome" in query:
            speak("What should I search ?")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "logout" in query:
            os.system("shutdown - l")
        
        elif "turn off" or "shut down" in query:
            os.system("shutdown /s /t 1")

        elif "restart" or "reboot" in query:
            os.system("shutdown /r /t 1")   

        elif "play songs" or "play a song" in query:
            songs_dir = "F:\Music files\ODESZA - A Moment Apart (Deluxe Edition) (2018) [320]" 
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" or "remeber to" in query:
            speak("What should I remember")
            data  = TakeCommand()
            speak("you wanted me to remind you about" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you want me to remind something" or "reminder" in query:
            remember = open("data.txt", "r")
            speak("you told me to remind you that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done and saved")

        elif "cpu" in query:
            cpu()
        
        elif "joke" in query:
            jokes()
        
        
            










