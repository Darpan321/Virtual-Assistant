import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import time
from googlesearch import search
import PyPDF2
import os
import sys

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
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'liz' in command:
                command = command.replace('liz', '')
                
    except:
        pass
    return command


def run_liz():
    command = take_command()
    
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'whatsapp message' in command:
        talk('Note this feature is for indian numbers')
        talk('So shall i proceed')
        permission1 = take_command()
        if 'yes' in permission1:
            talk('Can i get the number please')
            print("speak now")
            num1 = take_command()
            num= ["+91"+num1]
            talk('Can i get hour please')
            hour1=take_command()
            hour2=int(hour1)
            talk('Can i get minutes please')
            minute1=take_command()
            minute2=int(minute1)
            t2= [minute2]
            talk('What would you like to message')
            message1=take_command()
            for x in range(len(num)):
                t4=hour2
                t3=t2[x]
                pywhatkit.sendwhatmsg(num[x], message1 , t4, t3)
                x += 1
            
        else:
            talk('What other thing i can help you for')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'what is' or 'who is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'read a book' in command:
        path = "C://Users//darpa//Desktop//VT Project//books"
        fol_list = os.listdir(path)
        print(fol_list)
        talk('Which book would you like to read')
        bname1=take_command()
        pos=int(bname1)
        book = open(path+"/"+fol_list[pos], 'rb')
        talk('From which page number should i start from')
        spage1=take_command()
        spage2=int(spage1)
        talk('Till which page number shall i read')
        epage1=take_command()
        epage2=int(epage1)
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        
        speaker = pyttsx3.init()
        for num in range(spage2, epage2):
            page = pdfReader.getPage(num)
            text = page.extractText()
            speaker.say(text)
            speaker.runAndWait()
    elif 'search' in command:
        s1 = command.replace('search', '')
        for j in search(s1, tld="co.in", num=10, stop=10, pause=2):
            print(j)
        talk("I have found some quick links")

 

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'bye' in command:
        talk("Bye, Have a nice day")
        sys.exit()
    else:
        talk('Sorry i am getting new can you say the command again.')


while True:
    run_liz()

