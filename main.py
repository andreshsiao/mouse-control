import PySimpleGUI as sg
import pyautogui as ag

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
    [sg.Checkbox('Scroll Units', key='-Scroll-'), sg.InputText(key='-ScrollUnits-')],
    [sg.Text('(Positive numbers for scrolling up, negative for scrolling down)')],
    [sg.Text('Click Repeat')],
    [
    sg.Radio('Repeat','radio_repeat_settings', default=False, key='-Repeat-'),
    sg.InputText(key='-RepeatTimes-'), sg.Text('times') 
    ],
    [sg.Radio('Repeat until stopped', 'radio_repeat_settings', default=True, key='-RepeatTillStop-')],
    [
    sg.Button('Start', key='-Start-', disabled_button_color='gray'), 
    sg.Button('Stop', key='-Stop-', disabled=True, disabled_button_color='gray'), 
    sg.Button('Hotkey Setting', key='-HotkeySetting-', disabled_button_color='gray'), 
    sg.Cancel('Cancel', key='-Cancel-')]
]

window = sg.Window(title='Mouse Controller', layout=layout, margins = (100, 50))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '-Cancel-'):
        break

    if event == '-Start-':
        print(values) 
        window['-Start-'].update(disabled=True)
        window['-Stop-'].update(disabled=False)
        window['-HotkeySetting-'].update(disabled=True)

    if event == '-Stop-':
        window['-Start-'].update(disabled=False)
        window['-Stop-'].update(disabled=True)
        window['-HotkeySetting-'].update(disabled=False)

