# NAME = EMMANUEL APPIAH DEBRAH
# ID = 10956997 (FPEN)
import PySimpleGUI as sg
import pyttsx3

real = pyttsx3.init()

layout=[[sg.Text('Enter text to convert to speech'), 
            sg.InputText(key='-TEXT-'), sg.Button('Speak')],
        [sg.Text('Select Voice Type'), sg.Radio('Male', 'voice', default=True, key='-MALE-'),
           sg.Radio('Female', 'voice', key='-FEMALE-')],
        [sg.Text('Select Voice Rate:'),
           sg.Drop(values=[i for i in range(50, 501, 50)], default_value=[150], key='-RATE-')]
        ]

window = sg.Window('Text to Speech App', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['-TEXT-']
        real.setProperty('rate', values['-RATE-']) 
        real.setProperty('volume', 1.0) 
        voices = real.getProperty('voices')
        if values['-MALE-']:
            real.setProperty('voice', voices[1].id)
        elif values['-FEMALE-']:
            real.setProperty('voice', voices[0].id)

        
        real.say(text)
        real.runAndWait()

window.close()
real.stop()