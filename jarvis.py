import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning')
    elif hour >= 12 and hour < 16:
        speak('Goof afternoon')
    else:
        speak('Good evening')
    speak('I am jarvis, How can I help you?')

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('devikavarshneywork@gmail.com', 'xxxx')
    server.sendmail('devikavarshneywork@gmail.com', to, content)
    server.close()

def takeCommand():
    # takes microphone input and returns output as text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please..")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace('Wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            webbrowser.open('open.spotify.com')
            # music_dir=""
            # songs= os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # print("{strTime.hour}")
            speak(f"The time is {strTime}")
        elif "open code" in query:
            codePath = "C:\\devu\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "devikavarshney0003@gmail.com"
                sendEmail(to, content)
                speak('Email has been sent')
            except Exception as e:
                speak('Sorry email not sent')
        elif 'hello' in query:
            speak('Hy')
        elif 'how are you' in query:
            speak('I am fine what about you?')
        elif 'alexa' in query:
            speak('whooo is alexa? kon hai alexa batao?')
        elif 'siri' in query:
            speak('whooo is siri?')
        elif 'what\'s up' in query:
            speak('Nothing much you tell')
        elif 'love me' in query:
            speak('Yes very very much.')
        elif 'quit' in query:
            exit()
        elif "i am fine" in query:
            speak('wow, very good')
        elif 'thanks' in query:
            speak('you are welcome')

