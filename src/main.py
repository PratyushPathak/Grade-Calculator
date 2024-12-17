import functionality
import json
import PySimpleGUI as sg

try:
    with open('grades.json','x') as f:
        f.write("{}")
except FileExistsError:
    with open('grades.json', 'r') as readfile:
        grades = json.load(readfile)

try:
    with open('criteria.json','x') as g:
        g.write("{}")
except FileExistsError:
    with open('criteria.json', 'r') as openfile:
        criteria = json.load(openfile)

# All the stuff inside your window.
layout = []


# Create the Window
window = sg.Window('Grade Calculator', layout, size=(800, 600))


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    
    if(len(grades) == 0):
        while True:
            layout.append(sg.Text("Enter course name: "))
            layout.append(sg.Input("Text goes here"))
        
       
    

window.close()


