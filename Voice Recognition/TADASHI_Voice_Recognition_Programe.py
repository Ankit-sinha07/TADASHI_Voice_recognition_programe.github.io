# All the Modules that I have used in TADASHI.
from tokenize import Special
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#import smtplib Used for sending Emails.

#-------- Engine of Tadashi --------- 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# -----Speak Function------
def Speak(audio): # Speak Function
    engine.say(audio)
    engine.runAndWait()

#-----Greeting Function-------
def Greetfunc():
    hour = int(datetime.datetime.now().hour)
    if hour  >= 0 and hour < 12:
        Speak("Good Morning")
    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon")
    else:
        Speak("Good Evening")       

    Speak("Hello Sir My name is Tadashi and I am your Personal Assistant Created By Ankit Kumar Sinha")

# ----- Take Command Function------
# This command function takes voice command form the user and return the user request and also shows what the user had said.
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening, sir")
        Speak("Listening, sir")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("Recognizing Please give me a second!, sir")
        Speak("Recognizing Please give me a second!, sir")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please!")    
        Speak("Say that again please")  
        return "None"
    return query

#------------------------For sending Email----------------------------------------
#def sendEmail(to, content): # for this you have to allow less secure apps in your gamil account which you are using in your system
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login('youremail@gmail.com', 'your-password')
    #server.sendmail('youremail@gmail.com', to, content)
    #server.close()

if __name__ == "__main__":
    Greetfunc()
    while 2:
    #if 2:
        query = TakeCommand().lower() # Talking any command/query in lower string 

#Logic for excuting task's said by the User interface
#----------------------For Opening Most used web pages and software by the user------------------------------------------
        if 'wikipedia' in query: #Wikipedia
            Speak('Seraching on Wikipedia, Sir')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            Speak("This is what I've found sir")
            print(results)
            Speak(results)

        elif 'open youtube' in query: #Youtube
            Speak('opening Youtube sir')
            webbrowser.open("www.youtube.com")
        
        elif 'open google' in query: # Google
            Speak('opening Google sir')
            webbrowser.open("www.google.com")
        
        elif 'open stack overflow' in query: #Stack Overflow
            Speak("opening Stack Overflow sir")
            webbrowser.open("www.stackoverflow.com")

        elif 'open geeks for geek' in query: #Geeks For Geek
            Speak('opening Geeks for geek sir')
            webbrowser.open("www.geeksforgeeks.org")

        elif 'open game site' in query: # Game Site
            Speak('opening Fitgirl sir')
            webbrowser.open("https://fitgirl-repacks.site/")
        
        elif 'play music' in query: #Play Music
            Speak('opeaning Spotify sir')
            os.system('spotify')

#--------------------------For Opening Video Games--------------------------------------

        elif 'play games' in query: # Giving Choice to the user if the user have multiple games
            print('But Sir you have Multiple games, Which game you want me to open sir?')
            Speak('But Sir you have Multiple games, Which game you want me to open sir?')
            print('God of war')
            print('Days Gone')
            print('Horizon Zero Dawn')
            Speak('God of war, Days Gone, or Horizon Zero Dawn') 
            continue

        elif 'open god of war' in query: # God of war
            Speak('Opening God of War')
            game_dir = 'C:\\MY Files\\Games\\God of War\\GoW.exe'
            os.startfile(game_dir)
            break
        
        elif 'open days gone' in query: # Days Gone
            Speak('Opening Days gone')
            game_dir = 'C:\\MY Files\\Games\\Days Gone\\BendGame\\Binaries\\Win64\\DaysGone.exe'
            os.startfile(game_dir)
            break

        elif 'open horizon' in query: # Horizon zero dawn
            Speak('Opening Horizon zero dawn')
            game_dir = 'C:\\MY Files\\Games\\Horizon - Zero Down CE\\HorizonZeroDawn.exe'
            os.startfile(game_dir)
            break
    
#-----------------------------For telling the time-----------------------------------

        elif 'the time' in query: # This Function will tell us the date and time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            Speak(f"Sir, the time is {strTime}")
            break

#-----------------------------For opening Visual Studio code-------------------------
        elif 'open code editor' in query: # Visual Studio
            Speak('Opening Visual Studio code')
            print('Opening Visual Studio code')
            code_dir = 'C:\\Users\\sinha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(code_dir)
            break
#-----------------------------for Sending email--------------------------------
        #elif 'send email' in query:
            #try:
                #Speak("What you want to me to say, sir")
                #constant = TakeCommand
                #to = "etoosindia1145@gmail.com"
                #sendEmail(to, constant)
                #Speak("email has been send!")
            #except Exception as e:
                #print("There was an error sending your email, sir")