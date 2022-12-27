import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)


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
    while true:
        query = takeCommand().lower()
