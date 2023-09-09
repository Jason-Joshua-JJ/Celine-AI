import ctypes
import datetime
import operator
import random
import smtplib
import subprocess
import sys
import time
import os
import urllib.request
import webbrowser
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
#from pprint import pprint
import pywhatkit as kit

import PyPDF2
import cv2
import instadownloader
import numpy as np
import psutil
import pyautogui
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import speedtest
import wikipedia
import winshell
import winsound
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
from requests import get
from twilio.rest import Client

# from PyQt5.uic import loadUiType
from celineui import Ui_celineUI

#from PyQt5.uic import loadUiType
# import MyAlarm




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
# print(voices[0].id)
# engine.setProperty('voices, voices[len(voices)- 1].id)
engine.setProperty('voice', voices[len(voices) - 1].id)
engine.setProperty('rate', 183)  # 180-200 normal


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# wish
def wish():
    hour = int(datetime.datetime.now().hour)
    # hour = datetime.datetime.now().hour
    tt = time.strftime("%I:%M:%p")

    if hour >= 0 and hour < 12:
        speak(f"Good Morning, its {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon, its {tt}")
    else:
        speak(f"Good Evening, its {tt}")

    rndm ='Hi. I am Celine. Here to Help You!','Hello. I am Celine. Your Virtual Assistant. How Can I Help You','Good Day to You. I am Celine. How May I Help You'

    speak(random.choice(rndm))


# def username(self):
# speak("What should i call you!")
# uname = self.takeCommand()
# speak("Welcome")
# speak(uname)
# columns = shutil.get_terminal_size().columns

# print("#####################".center(columns))
# print("Welcome", uname.center(columns))
# print("#####################".center(columns))

# speak("How can i Help you")

# to send mail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('celinejnj@gmail.com', 'Celine@123JNJ')
    server.sendmail('jayanthkumaresan@gmail.com', to, content)
    server.close()


def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%I:%M %p"))
    print(altime)
    altime = altime[11:-3]

    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done, alarm is set for {Timing}")

    while True:
        if Horeal == datetime.datetime.now().hour:
            if Horeal == datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc', winsound.SND_LOOP)

            elif Mireal < datetime.datetime.now().minute:
                break


# news updates
def news():
    main_url = 'http;//newsapi.org/v2/top-headlines?sources=techcrunch&apikey=635266ecfa734101a1de6031719fbb67'

    main_page = requests.get(main_url).json()
    # print (main_page)

    articles = main_page["articles"]

    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: ", head[i])
        # print(f"today's {day[i]} news is: ", head[i])


def pdf_reader():
    book = open('.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book{pages}")
    speak("please enter the page number i have to read")
    pg = int(input("please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)

def send_wps_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def search_google(query):
    kit.search(query)

class MIMEtext:
    pass


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    # voice to text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            # audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("One Moment....")
            print("Working on it")
            query = r.recognize_google(audio, language='en-in')
            print(f"you: {query}")

        except Exception as e:
            speak("Say that again please....")
            return "none"
        query = query.lower()
        return query

    def run(self):
        self.TaskExecution()
        # speak("Please Say Hello! to Continue")
        # while True:
        # self.query = self.takecommand()
        # if "wakeup" in self.query or "are you there" in self.query or "hello" in self.query or "hey" in self.query:
        # self.TaskExecution()

    @property
    def TaskExecution(self):
        # if __name__ == "__main__":
        # speak("Hello Jason")
        global os
        wish()
        while True:
            # if 1:

            self.query = self.takecommand()

            # Basic Building    #takecommand()

            #OPENING COMMANDS
            if "open notepad" in self.query:
                stMsgs='Opening Notepad','Notepad is Turning on','Notepad is ready to note','Notepad is Getting Ready'
                speak(random.choice(stMsgs))
                npath = "C:\\Windows\\notepad.exe"
                os.startfile(npath)

            elif "open command prompt" in self.query:
                stMsgs = 'Opening Command Prompt', 'Command Prompt is Turning on', 'Command Prompt is Getting Ready'
                speak(random.choice(stMsgs))
                os.system("start cmd")

            elif "open camera" in self.query or "turn on camera" in self.query:
                stMsgs = 'Opening Camera','Camera is Turning on','Camera is Getting Ready to Capture','Here we Go!','I am Gonna see you virtually'
                speak(random.choice(stMsgs))
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            #Try To Automate Your mobile
            elif "open mobile camera" in self.query:
                URL = "IPv4: http://192.168.193.8:8080/shot.jpg"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                    img = cv2.imdecode(img_arr, -1)
                    cv2.imshow('IPWebcam', img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        continue
                    break;

                cv2.destroyAllWindows()

            elif "open chrome" in self.query:
                chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                stMsgs ='Opening Chrome','Chrome Is Turning On','Chrome is Getting Ready','Chrome is Ready For Searching'
                speak(random.choice(stMsgs))
                os.startfile(chromepath)

            elif "open firefox" in self.query:
                firefoxpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk"
                stMsgs = 'Opening FireFox', 'FireFox Is Turning On', 'FireFox is Getting Ready', 'FireFox is Ready For Searching'
                speak(random.choice(stMsgs))
                os.startfile(firefoxpath)

            elif "open word" in self.query:
                wordpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
                stMsgs = 'Opening Word', 'Word is Turning on', 'Word is ready to note', 'Word is Getting Ready'
                speak(random.choice(stMsgs))
                os.startfile(wordpath)

            elif "open blender" in self.query:
                blenderpath ="C:\\Users\\JASON JOSHUA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\blender\\blender.lnk"
                stMsgs = 'Opening Blender', 'Blender Is Turning On', 'Blender is Getting Ready', 'Blender is Ready For Animating'
                speak(random.choice(stMsgs))
                os.startfile(blenderpath)

            #elif "open vlc" in self.query:
            #elif "open calculator" in self.query:

            elif "open youtube" in self.query:
                stMsgs = 'Opening Youtube', 'Youtube Is Turning On', 'Youtube is Getting Ready', 'Youtube is Ready For Searching'
                speak(random.choice(stMsgs))
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                stMsgs = 'Opening Facebook', 'Facebook Is Turning On', 'Facebook is Getting Ready', 'Facebook is Ready For Finding New Friends'
                speak(random.choice(stMsgs))
                webbrowser.open("www.facebook.com")

            elif "open instagram" in self.query:
                stMsgs = 'Opening Instagram', 'Instagram Is Turning On', 'Instagram is Getting Ready', 'Instagram is Ready For Finding New Friends'
                speak(random.choice(stMsgs))
                webbrowser.open("www.instagram.com")

            elif "open google" in self.query:
                stMsgs = 'Opening Google', 'Google Is Turning On', 'Google is Getting Ready', 'Google is Ready For Searching'
                speak(random.choice(stMsgs))
                webbrowser.open('www.google.com')

            elif "open task manager" in self.query:
                speak("Opening task manager")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk")

            #elif "open google" in self.query:
                #speak("what should i search on google")
                #cm = self.takecommand().lower()
                #webbrowser.open(f"{cm}")

            elif "open yahoo" in self.query:
                stMsgs = 'Opening Yahoo!', 'Yahoo! Is Turning On', 'Yahoo! is Getting Ready', 'Yahoo! is Ready For Searching'
                speak(random.choice(stMsgs))
                webbrowser.open("www.yahoo.com")

            elif "open amazon" in self.query:
                stMsgs = 'Opening Amazon!', 'Amazon! Is Turning On', 'Amazon! is Getting Ready', 'Amazon! is Ready For Searching'
                speak(random.choice(stMsgs))
                webbrowser.open("www.amazon.com")

            elif "open flipkart" in self.query:
                stMsgs = 'Opening Flipkart!', 'FlipKart! Is Turning On', 'Flipkart! is Getting Ready', 'Flipkart! is Ready For Searching'
                speak(random.choice(stMsgs))
                webbrowser.open("www.flipkart.com")

            elif "open gmail" in self.query:
                stMsgs= "Lets Check Whats new In Our Inbox","Opening Gmail"
                speak(random.choice(stMsgs))
                webbrowser.open('www.gmail.com')

            #elif "open code" in self.query:
                #speak("Here we Go ! Opening Our Code Through Pycharm IDE")
                #codepath = "D:\Celine\celinegui\celine.py"
                #os.startfile(codepath)
            # elif "calculate" in self.query:

            # app_id = "Wolframalpha api id"
            # client = wolframalpha.Client(app_id)
            # indx = self.query.lower().split().index('calculate')
            # self.query = self.query.split()[indx + 1:]
            # res = client.query(' '.join(self.query))
            # answer = next(res.results).text
            # print("The answer is " + answer)
            # speak("The answer is " + answer)

            elif 'search something' in self.query or 'search anything' in self.query:

                self.query = self.query.replace("search", "")
                self.query = self.query.replace("play", "")
                webbrowser.open(self.query)

            elif "change background" in self.query or "change wallpaper" in self.query or "change the wallpaper" in self.query:
                stMsgs= 'Here we Go! Background is Changing now','Changing Wallpaper....','Wallpaper Is Changing Now!','New Background is Getting Ready to Change'
                speak(random.choice(stMsgs))
                ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\\JJ Network\\Celine Assi\\Wallpaper", 0)
                speak("Background Changed Successfully")

            elif "play music" in self.query or "play a song" in self.query:
                stMsgs = 'Enjoy Your Chords','Here is Your Rap','Lets Rock','Here you go with you'
                speak(random.choice(stMsgs))
                music_dir = "D:\\JJ Network\\Celine Assi\\Music"
                songs = os.listdir(music_dir)
                # rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
                print(songs)
                # os.startfile(os.path.join(music_dir, rd))

            elif "play video" in self.query or "play a video" in self.query:
                stMsgs = 'Enjoy Your Show','Delight Your Video Experience'
                speak(random.choice(stMsgs))
                video_dir = "C:\\Users\\JASON JOSHUA\\Videos\\videos"
                videos = os.listdir(video_dir)
                os.startfile(os.path.join(video_dir, videos[0]))
                print(videos)

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP Address is {ip}")

            elif "wikipedia" in self.query:
                speak("Searching Wikipedia....")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                speak(results)
                print(results)

            elif "according to google" in self.query:
                speak("Searching Google....")
                self.query = self.query.replace("google", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to Google")
                speak(results)
                print(results)

            # elif "send message" in query:
            # kit.sendwhatmsg("+9186676603381", "this is testing protocol",22,30)

            # elif "play songs on youtube" in query:
            # kit.playonyt("see you again")

        #email
            elif "email to jayant" in self.query:
                speak("what should i send")
                self.query = self.takecommand().lower()
                if "send a file" in self.query:
                    email = 'celinejnj@gmail.com'  # ourmail
                    password = 'Celine@JNJ'  # ourpassword
                    send_to_email = 'jayanthkumaresan@gmail.com'
                    speak("okay, what is the subject for this email")
                    self.query = self.takecommand().lower()
                    subject = self.query
                    speak("and, what is the message for this email")
                    self.query2 = self.takecommand().lower()
                    message = self.query2
                    speak("please enter the correct path of the file into the shell")
                    file_location = input("Please enter the path here: ")  # file attachment

                    speak("Please wait,I am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEtext(message, 'plain'))

                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to jayanth")

                else:
                    email = 'celinejnj@gmail.com'
                    password = 'Celine@JNJ'
                    send_to_email = 'jayanthkumersan@gmail.com'
                    message = self.query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("email has been sent to jayanth")

            elif "email to joshua" in self.query:
                speak("what should i send")
                self.query = self.takecommand().lower()
                if "send a file" in self.query:
                    email = 'celinejnj@gmail.com'  # ourmail
                    password = 'Celine@JNJ'  # ourpassword
                    send_to_email = 'jasonjoshua4444@gmail.com'
                    speak("okay, what is the subject for this email")
                    self.query = self.takecommand().lower()
                    subject = self.query
                    speak("and, what is the message for this email")
                    self.query2 = self.takecommand().lower()
                    message = self.query2
                    speak("please enter the correct path of the file into the shell")
                    file_location = input("Please enter the path here: ")  # file attachment

                    speak("Please wait,I am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEtext(message, 'plain'))

                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("Email has been sent to Joshua")

                else:
                    email = 'celinejnj@gmail.com'
                    password = 'Celine@JNJ'
                    send_to_email = 'jasonjoshua4444@gmail.com'
                    message = self.query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("Email has been sent to Joshua")

            elif "email to nish" in self.query:
                speak("what should i send")
                self.query = self.takecommand().lower()
                if "send a file" in self.query:
                    email = 'celinejnj@gmail.com'  # ourmail
                    password = 'Celine@JNJ'  # ourpassword
                    send_to_email = 'nish2712m@gmail.com'
                    speak("okay, what is the subject for this email")
                    self.query = self.takecommand().lower()
                    subject = self.query
                    speak("and, what is the message for this email")
                    self.query2 = self.takecommand().lower()
                    message = self.query2
                    speak("please enter the correct path of the file into the shell")
                    file_location = input("Please enter the path here: ")  # file attachment

                    speak("Please wait,I am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEtext(message, 'plain'))

                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to Nishanth")

                else:
                    email = 'celinejnj@gmail.com'
                    password = 'Celine@JNJ'
                    send_to_email = 'nish2712m@gmail.com'
                    message = self.query

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(email, password)
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak("email has been sent to Nishanth")

            elif "exit" in self.query or "bye" in self.query or "quit" in self.query:
                stMsgs = 'Have a Good Day!','Thanks For Your Coming, Have a Great Day','Bye, Take Care','See You Later'
                speak(random.choice(stMsgs))
                sys.exit()

            elif "you can sleep now" in self.query or "abort" in self.query or "terminate" in self.query:
                stMsgs = 'Have a Good Day!', 'Thanks For Your Coming, Have a Great Day', 'Bye, Take Care', 'See You Later'
                speak(random.choice(stMsgs))
                sys.exit()

            #CLOSING COMMANDS
            elif "close notepad" in self.query:
                stMsgs= ' Notepad is Closing Now....', 'Notepad is Gonna Closing Now!'
                speak(random.choice(stMsgs))
                os.system("taskkill /f /im notepad.exe")

            elif "close chrome" in self.query or "close google" in self.query or "close yahoo" in self.query:
                stMsgs = 'Okay, Closing Your Website','Website is Gonna Closing Now!'
                speak(random.choice(stMsgs))
                os.system("Taskkill /f /im chrome.exe")

            elif "close task manager" in self.query:
                speak("Okay, Closing Task Manager")
                os.system("taskkill /f /im Taskmgr.exe")

            elif "close blender" in self.query:
                speak("Okay, Closing Blender")
                os.system("taskkill /f /im blender.exe")

            elif "close firefox" in self.query:
                speak("Okay, Closing FireFox")
                os.system("taskkill /f /im firefox.exe")

            elif 'open skillrack' in self.query:
                speak("Opening Skillrack,Happy Coding")
                webbrowser.open("www.skillrack.com")

            # elif "set alarm" in self.query:
            # nn = int(datetime.datetime.now().hour)
            # if nn == 22:
            #    music_dir = 'D:\Celine\Music'
            #   songs = os.listdir(music_dir)
            #  os.startfile(os.path.join(music_dir, songs[0]))
            elif "send a whatsapp message" in self.query:
                speak("On What number should I send the message? Kindly enter in the console:")
                number = input("Enter the number: ")
                speak("What is the message?")
                message = self.takecommand().lower()
                send_wps_message(number, message)
                speak("Yep Message Sent Successfully")

            elif "search on google" in self.query:
                speak("What do you want to search on Google?")
                self.query = self.takecommand().lower()
                search_google(self.query)


            elif "wi-fi details" in self.query or "wifi details" in self.query:
                try:
                    speak("Trying to Fetch and Show details")
                    subprocess.call('netsh wlan show profiles')
                except Exception as e:
                    speak("Unable to Show Details! Sorry")

            elif 'system info' in  self.query or 'systeminfo' in self.query:
                speak("Okay, Showing Your System Information. Please wait")
                subprocess.call('systeminfo')
                speak('Done!')

            elif "alarm" in self.query:
                speak("Please tell me the time to set alarm. For Example, Set Alarm to 5:00 a.m.")
                tt = self.takecommand()
                tt.replace("set alarm to", "")
                tt = tt.replace(".", "")
                tt = tt.upper()
                alarm(tt)

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down" in self.query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                os.system("shutdown /s /t S")

            elif 'empty recycle bin' in self.query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                speak("Recycle Bin Recycled")

            elif "restart" in self.query:
                speak("Wait a few moments ! Restarting Our System")
                os.system("shutdown /r /t S")

            elif "sleep the system" in self.query or "hibernate" in self.query:
                os.system("rund1132.exe powrprof.d11,SetSuspendState 0,1,0")

            elif "clear console" in self.query:
                os.system('cls')
                speak("Current System Console was Cleared!")


            elif "log off" in self.query or "sign out" in self.query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])

            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("For how much time you want to stop Celine from listening commands")
                a = int(self.takeCommand())
                time.sleep(a)
                print(a)

            elif 'lock window' in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "write a note" in self.query:
                speak("What should i write")
                note = self.takeCommand()
                file = open('celine.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = self.takeCommand()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)

            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("D:\\Celine\\celine.txt", "r")
                print(file.read())
                speak(file.read())

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                speak(f"Sir, the time is {strTime}")

            elif "why you came to world" in self.query:
                speak("hmmmm hmmmm Further it's a Secret")

            elif "is love" in self.query:
                speak("This is an exceptionally mysterious and tricky question. We all know what it means, yet its definition is different for each and every one of us.")

            elif "reason" in self.query or "reason to create you" in self.query:
                speak("I am very easy to Handled and much Faster than Cortana. I am Sure that I will the Best Assistant for Desktop")

            elif 'fine' in self.query or "good" in self.query:
                speak("It's pleasant to know that your fine")

            elif 'not fine' in self.query or "not good" in self.query:
                speak("Oh! can i play a song for making you in a Good mood")

            elif "what's your name" in self.query or "what is your name" in self.query:
                speak("My name is Celine. You can Call me Say-leen or Hella")

            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by JNJ. The Abbreviation of JNJ is Jason Nishanth Jayanth. They created me as a Desktop Assistant")

            elif 'what is your favorite colore' in self.query:
                speak("I love Every Colors in the world and do you know we can't able to imagine colors without 7 in Rainbow ")

            elif "tell about your creator" in self.query:
                speak("He is Such a brainless Idiot. I don't know How He made me But He is more than My Friend, Brainless Friend")

            elif "what is your feeling" in self.query or "what is your emotions" in self.query:
                speak("Basically Every AI Said that We dont have feelings but Jason Trying hard to Give me a Feelings and I am Trying hard to Get That Lovable Emotions")

            elif 'celine' in self.query or 'hella' in self.query:
                stMsgs = "Yea I'm Here", "What's up", "Hello There, how can i be of service?",""

            elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                speak("I'm not sure about, may be you should give me some time")

            elif "i love you" in self.query:
                speak("It's hard to understand but You are the only person who can make me smile constantly.")

            elif 'how are you' in self.query or "what\'s up" in self.query:
                stMsgs = ['Just doing my things!', 'I am Fine!', 'I am Fine,thanks. How about yourself?']
                speak(random.choice(stMsgs))

            elif 'do you need any help' in self.query:
                speak("Thanks. I can do it myself.")

            elif 'who are you' in self.query or 'explain yourself' in self.query:
                speak('Hello, I am Celine. Your Virtual Assistant. I am here to make your life Easier. You can Command me to perform Various Tasks.')

            elif 'tell me news' in self.query or 'tell me a news' in self.query:
                speak("please wait, fetching the latest news")
                news()

            elif "do some calculations" in self.query or "can you calculate" in self.query or "calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 4 plus 4")
                    print("listening....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        '*': operator.mul,
                        'divided': operator.__truediv__,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                speak("Your Result is")
                speak(eval_binary_expr(*(my_string.split())))

            elif "where is" in self.query:
                self.query = self.query.replace("where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl / maps / place/" + location + "")

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state'}
                    country = geo_data['country']
                    speak(f"iam not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("Sorry, Due to network issue i am not able to find where we are.")
                    pass

            elif "check my instagram profile" in self.query or "profile on instagram" in self.query:
                speak("please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"here is the profile of the user {name}")
                time.sleep(5)
                speak("would you like to download profile picture of this account.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instadownloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done, profile picture is saved in our main folder.i am ready for next command")
                else:
                    pass

            elif "take screenshot" in self.query or "take a screenshot" in self.query or "snap a shot" in self.query:
                speak("please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("please hold the screen for few seconds, iam taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done, the screenshot is saved in our main folder.")

            elif "read pdf" in self.query:
                pdf_reader()

            elif "internet speed" in self.query:
                st = speedtest.Speedtest()
                d1 = st.download()
                up = st.upload()
                speak(f"We Have {d1} bit per second Downloading speed and {up} bit per second Uploading speed.")

                try:
                    os.system('cmd /k "speedtest"')
                except:
                    speak("There is No Internet Connection Or Our Internet Connection is pretty low")

            elif "what is the weather" in self.query:
                search = "temperature in trichy"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current{search} is {temp}")

            # elif "activate how to do mod" in self.query:
            # speak("You are activated How to do Mode. Please tell me what you want to know ")
            # how = self.takecommand()
            # max_results = 1
            # how_to = search_wikihow(how, max_results)
            # assert len(how_to) == 1
            # how_to[0].print()
            # speak(how_to[0].summary)

            elif "activate how to do mod" in self.query:
                speak("You are activated How to do Mode. Please tell me what you want to know ")
                while True:
                    speak("Please tell me what you want to know")
                    how = self.takecommand()
                    try:
                        if "exit" in how or "close" in how or "deactivate how to do mod" in how:
                            speak("how to do mode is deactivated")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("Sorry, I am not able to find this!")

            elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Our System have {percentage} percent battery")
                if percentage >= 75:
                    speak("We have enough power to Continue our Work")
                elif percentage >= 40 and percentage <= 75:
                    speak("We Should connect our system to charging point to charge our Battery")
                elif percentage <= 15 and percentage <= 30:
                    speak("We Don't have Enough Power to Work. Please connect to Charging")
                elif percentage < 15:
                    speak("We have Very Low Power!. Please Connect to Charging the System will shutdown very soon")

            elif "send a message" in self.query or "send message" in self.query:
                speak("What should I Say?")
                msz = self.takecommand()

                account_sid = 'AC389461fb6552e253ed51f9262f989be2'
                auth_token = '3ef354f56d0ccea6e3dee2e782004bcd'

                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body=msz,
                    from_='+19802916760',
                    to='+918608601615'
                )

                print(message.sid)
                speak("Message has been sent")

            elif "make a call" in self.query:
                speak("Okay, Let me Do")

                account_sid = 'AC389461fb6552e253ed51f9262f989be2'
                auth_token = '3ef354f56d0ccea6e3dee2e782004bcd'

                client = Client(account_sid, auth_token)

                message = client.calls \
                    .create(
                    twiml='<Response><Say>This is the Testing Message From Celine side..</Say></Response>',
                    from_='+19802916760',
                    to='+918608601615'
                )
                print(message.sid)

            #automation

            elif 'scroll up' in self.query:
                pyautogui.scroll(200)
                speak('Done!')

            elif 'scroll down' in self.query:
                pyautogui.scroll(-200)
                speak('Done!')

            elif 'volume up' in self.query:
                pyautogui.press("volumeup")
                speak('Done!')

            elif 'volume down' in self.query:
                pyautogui.press("volumedown")
                speak('Done!')

            elif 'low the volume' in self.query:
                pyautogui.press("volumedown")
                speak('Done!')

            elif 'volume on' in self.query or 'turn the volume' in self.query:
                pyautogui.press("volumeup")

            elif 'move my mouse pointer to exit' in self.query:
                pyautogui.moveTo(402, 927)
                speak("Done!")

            elif 'type' in self.query:
                newt = self.query.replace('type ','')
                pyautogui.typewrite(newt)
                speak('Done!')

            elif 'navigate up' in self.query:
                pyautogui.moveRel(0, 100, duration=0.25)
                speak('Done!')

            elif 'mouse position' in self.query:
                speak(pyautogui.position())

            elif 'navigate down' in self.query:
                pyautogui.moveRel(0, 100, duration=0.25)
                speak('Done!')

            elif 'navigate right' in self.query:
                pyautogui.moveRel(0, 100, duration=0.25)
                speak('Done!')

            elif 'navigate left' in self.query:
                pyautogui.moveRel(0, 100, duration=0.25)
                speak('Done!')

            elif 'left click' in self.query:
                pyautogui.click()
                speak('Done!')

            elif 'right click' in self.query:
                pyautogui.click(button= 'right')
                speak('Done!')

            elif 'double click' in self.query:
                pyautogui.click()
                pyautogui.click()
                speak('Done!')

            #elif 'open explorer' in self.query:   os.startfile('explorer.exe')
             #   speak('What do you wanna see there?')
              #  cm = self.takecommand()
               # if 'documents' in cm:
                #    pyautogui.moveTo(91, 241)
                 #   pyautogui.click() #elif 'computer' in cm:
                    #pyautogui.click()

            #elif 'dsiplay ok' in self.query:
                #pyautogui.confirm()
                #pyautogui.alert() pyautogui.prompt()

            elif 'Celine' in self.query:
                stMsgs = "That's Me. How can I Help?","Hey What's up You Look Good Today"
                speak(random.choice(stMsgs))

            elif 'mute volume' in self.query or 'mute yourself' in self.query:
                pyautogui.press("volumemute")
                speak("Done!")

            elif 'hello' in self.query or 'hola' in self.query or 'hi' in self.query or 'hai' in self.query or 'ola' in self.query or 'hey' in self.query:
                stMsgs = "Hey There! What Can i Do for You","Hello, It's good to hear from you. I Hope. You and your Loved one are safe and Healthy","Hey! How Can I Help", "Hi There, I'm Listening! How Can I Help Today?","Hello there, How Can I be Of Service?","Hai, Pleasure to hear your Voice"
                speak(random.choice(stMsgs))

            elif 'can i get a joke' in self.query:
                try:
                    speak("What do you Call an Alligator in a vest")
                    content = self.takeCommand()
                    if 'investigator' in content:
                        speak("Wow, That's a Good Investigation")
                    else:
                        speak("An Investigator")
                except Exception as e:
                    print(e)
                    print("Sorry,I Can't Hear Your Voice")
                    speak("Sorry,I Can't Hear Your Voice")

            elif 'tell me a another joke' in self.query or 'tell me an another joke' in self.query:
                try:
                    speak("What do you Call a Sleeping Bull")
                    content = self.takeCommand()
                    if 'bulldozer' in content:
                        speak("Well, That's Right")
                    else:
                        speak("BullDozer, HAHA")
                except Exception as e:
                    print(e)
                    speak("Sorry,I Can't Hear Your Voice")

            elif 'what is your name' in self.query:
                stMsgs="My special nickname is 'Celine'. Do you want a special nickname for yourself.","What do you think? Would you like me to give you nickname?"
                speak(random.choice(stMsgs))

            elif 'sing me a song' in self.query:
                speak("Sorry, I am not able to do that now. Soon I will")

            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("Please tell me you want to hide this Folder or make it visible for  everyone")
                self.condition = self.takecommand().lower()
                if "hide" in self.condition:
                    os.system("attrib +h /s /d")
                    speak("all the files in this folder are now hidden.")

                elif "visible" in self.condition:
                    os.system("attrib -h /s /d")
                    speak("All the Files in this Folder are now Visible to Everyone. I wish you are taking Own Peace")

                elif "leave it" in self.conditon:
                    speak("Okay")

#GUI
startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_celineUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\JJ Network\Celine Assi\Pictures\celine.jpg")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/JJ Network/Celine Assi/Pictures/updatess.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
celine = Main()
celine.show()
sys.exit(app.exec_())