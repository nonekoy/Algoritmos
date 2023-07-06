import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import read_all_windows

def lay1():
        sg.theme('Black')
        tela =[[sg.Text('Digite aí seu feio:')],
                 [sg.InputText()],
                 [sg.Button('OK'), sg.Button('Quit')]    
                ]
        return sg.Window('tela 1', layout= tela, finalize = True)

def lay2():
        sg.theme('Black')
        tela =[[sg.Text('consegui')]
                
                ]
        return sg.Window('tela 2', layout= tela, finalize = True)

while True:
        layout = lay1(), None
        window, event, value = read_all_windows()
        if event in (sg.WIN_CLOSED, 'Quit'):
                break
        if event in (window, 'OK'):
                layout= lay2


window.close()    
