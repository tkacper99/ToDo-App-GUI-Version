import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("data.txt"):
    with open("data.txt", "w")as file:
        pass

sg.theme("DarkPurple4")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip="Enter todo", key="todoItem")
addButton = sg.Button("Add")
todosListBox = sg.Listbox(values=functions.get_todos(),
                          key="todoListbox",
                          enable_events=True,
                          size=[45, 10])

editButton = sg.Button("Edit")
completeTaskButton = sg.Button("Complete")
exitButton = sg.Button("Exit")

window = sg.Window('To Do App',
                   layout=[[clock],
                           [label],
                           [inputBox, addButton],
                           [todosListBox, editButton, completeTaskButton],
                           [exitButton]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        # Add button case
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todoItem'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

            window['todoListbox'].update(values=todos)
        # Edit button case
        case "Edit":
            try:
                todoToEdit = values['todoListbox'][0]
                new_todo = values['todoItem'] + "\n"

                todos = functions.get_todos()
                todoToEditIndex = todos.index(todoToEdit)

                todos[todoToEditIndex] = new_todo
                functions.write_todos(todos)

                window['todoListbox'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 20))
        # Case for completing a task
        case "Complete":
            try:
                todoToComplete = values['todoListbox'][0]

                todos = functions.get_todos()
                todos.remove(todoToComplete)
                functions.write_todos(todos)

                window['todoListbox'].update(values=todos)
                window['todoItem'].update(value="")
            except IndexError:
                sg.popup("Please select an item first!", font=("Helvetica", 20))
        case 'Exit':
            break
        # Case for changing viewed text in Input placeholder
        case 'todoListbox':
            window['todoItem'].update(value=values['todoListbox'][0])
        # Case for closing application
        case sg.WIN_CLOSED:
            break

window.close()
