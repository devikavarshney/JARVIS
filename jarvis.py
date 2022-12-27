import datetime
import pyttsx3
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
if __name__ == "__main__":
    wishMe()
