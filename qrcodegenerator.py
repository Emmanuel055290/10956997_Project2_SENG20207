# NAME = EMMANUEL APPIAH DEBRAH
# ID = 10956997 (FPEN)

import pyqrcode
import PySimpleGUI as sg


#Defining a list of basic colors in order to produce QRcode in different colours
COLORS = ['Black', 'White', 'Red', 'Green', 'Blue', 'Yellow', 'Magenta', 'Cyan']

# Designing the layout of the User Interface
layout = [[sg.Text('Enter text to generate QR Code')],
          [sg.InputText(key='-TEXT-')],
          [sg.Text('Color: '), sg.InputCombo(COLORS, size=(20, 1), key='-COLOR-')],
          [sg.Button('Create QR Code'), sg.Button('Exit')],
          [sg.Image(key='-IMAGE-')]]

# Create the window
window = sg.Window('QR Code Generator', layout)

# Loop to handle events and get user input
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Create QR Code':
        # Get the selected color
        color_name = values['-COLOR-']
        if color_name == 'Black':
            hex_code = '#000000'
        elif color_name == 'White':
            hex_code = '#FFFFFF'
        elif color_name == 'Red':
            hex_code = '#FF0000'
        elif color_name == 'Green':
            hex_code = '#00FF00'
        elif color_name == 'Blue':
            hex_code = '#0000FF'
        elif color_name == 'Yellow':
            hex_code = '#FFFF00'
        elif color_name == 'Magenta':
            hex_code = '#FF00FF'
        elif color_name == 'Cyan':
            hex_code = '#00FFFF'

        # Code to validate the input text
        if not values['-TEXT-']:
            sg.popup_error('Please enter some text to generate the QR code')
            continue

        # Code to check if the input text is a valid URL
        if values['-TEXT-'].startswith('http://') or values['-TEXT-'].startswith('https://') or values['-TEXT-'].startswith('www.'):
            text = values['-TEXT-']
        else:
            sg.popup_error('Invalid URL. Please enter a valid URL starting with http:// or https:// or www.')
            continue

        # Creating a feature for the QR code with customized color and size
        qr = pyqrcode.create(text)
        qr.png('qrcode.png', module_color=hex_code, background=[255, 255, 255, 255], scale=10)

        # Update the image element in the window
        window['-IMAGE-'].update(filename='qrcode.png')

window.close()