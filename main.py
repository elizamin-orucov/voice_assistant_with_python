import speech_recognition as sp_r
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
from dictionary import words


r = sp_r.Recognizer()


def record(ask=False):

    with sp_r.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ""

        try:
            voice = r.recognize_google(audio, language="en-EN")

        except sp_r.UnknownValueError:
            speak("I don't understand")

        except sp_r.RequestError:
            speak("System is not working")
        return voice


def speak(data):
    tts = gTTS(data, lang="en")
    rand = random.randint(1, 10000)

    file_ = f"audio-{str(rand)}.mp3"
    tts.save(file_)
    playsound(file_)
    os.remove(file_)


speak("The program has been launched, how can I help you?")
time.sleep(1)

while 1:
    text = record().lower()
    print("You: ", text)

    if text in words.keys():
        answer = words[text]
        speak(answer)

    elif text == "do search":
        search = record("what do you want to search")
        url = f"https://google.com/search?q={search}"
        webbrowser.get().open(url)
        speak(f"search results for {search}")

    elif text == "exit":
        speak("OK, exiting program")
        exit()