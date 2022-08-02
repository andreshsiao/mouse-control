import mouse
import PySimpleGUI as sg


sg.theme('Sandy Beach')

layout = [
    [sg.Text('Click Options')],
    [
    sg.Text('Mouse Button:'), 
    sg.Radio('Left', 'radio_mouse_button', default=True, key='-Left-'),
    sg.Radio('Right', 'radio_mouse_button', default=False, key='-Right-'),
    sg.Radio('Middle', 'radio_mouse_button', default=False, key='-Middle-'),    
    ],
    [
    sg.Text('Click Type:'),
    sg.Radio('Single', 'radio_click_type', default=True, key='-Single-'),
    sg.Radio('Double', 'radio_click_type', default=False, key='-Double-')
    ],
    [sg.Text('Click Interval:')],
    [
    sg.Text('min:'), sg.InputText(size=(5,1), key='-Min-'), 
    sg.Text('second:'), sg.InputText(size=(5,1), key='-Sec-'), 
    sg.Text('ms:'), sg.InputText(size=(5,1), key='-Ms-')
    ],
    [sg.Text('Wheel Scroll:')],
    [sg.Checkbox('Scroll Units'), sg.InputText(key='-ScrollUnits-')],
    [sg.Text('(Positive numbers for scrolling up, negative for scrolling down)')],
    [sg.Text('Click Repeat')],
    [
    sg.Radio('Repeat','radio_repeat_settings', default=False, key='-Repeat-'),
    sg.InputText(key='-RepeatTimes-'), sg.Text('times') 
    ],
    [sg.Radio('Repeat until stopped', 'radio_repeat_settings', default=True, key='-RepeatTillStop-')],
    [sg.Button('Start'), sg.Button('Stop'), sg.Button('Hotkey Setting'), sg.Button('Cancel')]
]

# window = 
window = sg.Window(title='Mouse Controller', layout=layout, margins = (100, 50))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Start':
        print(values) 
        if values['-Right-']:
            mouse.click('Right')
        elif values['-Left-']:
            mouse.click('Left')
        else:
            mouse.click('Middle')


