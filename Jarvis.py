import speech_recognition
import os
import webbrowser
import playsound
import Log
#
alias = ""

commands = {
    "time": (""),
    "new folder": ("")
}

#Speaking
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listening():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            return query
    except:
        return ""

#
def verification(cmd):
    if cmd.startswith(alias):
        cmd = cmd.replace(alias, "").strip()
        search_commands(cmd)

def search_commands(text):
    if text.startswith(commands["time"]):
        print("Hello!")

verification("")