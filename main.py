import speech_recognition as sp_r
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
from dictionary import words
import random
import os


rcognizer = sp_r.Recognizer()


def record(ask=False):

    with sp_r.Microphone() as microphone_sound:
        if ask:
            speak(ask)
        audio = rcognizer.listen(microphone_sound)
        voice = ""

        try:
            voice = rcognizer.recognize_google(audio, language="en-EN")

        except sp_r.UnknownValueError:
            speak("I don't understand")

        except sp_r.RequestError:
            speak("System is not working")
        return voice


def speak(data):
    sound_file = gTTS(data, lang="en")
    rand = random.randint(1, 10000)

    sound_file_name = f"audio-{str(rand)}.mp3"
    sound_file.save(sound_file_name)
    playsound(sound_file_name)
    os.remove(sound_file_name)


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
