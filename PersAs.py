#!/usr/local/bin/python3

"""
>>>> Really buggy at the moment
"""

import wolframalpha
import PySimpleGUI as sg
import pyttsx3

sg.theme("DarkBlue")
layout = [  [sg.Text("How can I help you?", size=(60, 1), justification="center", font=("Helvetica", 15))],
            [sg.Input(size=(60, 1), font=("Helvetica", 15))],
            [sg.Button("Search", font=("Helvetica", 15)), sg.Button("Cancel", font=("Helvetica", 15))]
            ]
window = sg.Window("PersAs - Your Personal Assistant", layout, size=(450, 100), element_justification="center")
client = wolframalpha.Client("Your Access Token") # MUST KEPT PRIVATE
engine = pyttsx3.init()

volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break

    res = client.query(values[0])
    try:
        sg.PopupNonBlocking(next(res.results).text, title="Information", font=("Helvetica", 15))
        engine.say(next(res.results).text)
        try:
            engine.runAndWait()
        except:
            pass
    except:
        sg.PopupNonBlocking("I am sorry, but no Information was found.", title="Error", font=("Helvetica", 15))
        engine.say("I am sorry, but no Information was found.")
        try:
            engine.runAndWait()
        except:
            pass

window.close()
