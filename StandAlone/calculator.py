#  ## Simple Calculator with 9 digits and 12 function ##
from tkinter import *
import parser
from functools import partial

i = 0  # used in the calculator button functions


def calculate(dmy):
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all(dmy)
        display.insert(0, result)
    except:
        clear_all(dmy)
        display.insert(0, "Error")


def clear_all(dmy):
    display.delete(0, END)


def undo(dmy):
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all(dmy)
        display.insert(0, new_string)
    else:
        clear_all(dmy)
        display.insert(0, "Error")


def get_keypress(value):
    global i
    length = len(value)
    display.insert(i, value)
    i += length


mainWindow = Tk()
mainWindow.title("Calculator")

# configure 5 rows with varying weights
rowWeights = [5, 20, 20, 20, 20]
for rr in range(0, 5):
    mainWindow.rowconfigure(rr, weight=rowWeights[rr])

# configure 6 equal columns
for cc in range(0, 6):
    mainWindow.columnconfigure(cc, weight=1)

# row 0 - input (display) box
display = Entry(mainWindow)
display.grid(row=0, column=0, columnspan=6, sticky='nswe')

# 4 rows (after the entry box row 0) and 6 columns in each row
# row: [('text', 'command function', 'function parameter')]
calcButtons = {
    1: [['7', 'get_keypress', '7'], ['8', 'get_keypress', '8'], ['9', 'get_keypress', '9'],
        ['/', 'get_keypress', '/'], ['AC', 'clear_all', ''], ['<-', 'undo', '']],
    2: [['4', 'get_keypress', '4'], ['5', 'get_keypress', '5'], ['6', 'get_keypress', '6'],
        ['*', 'get_keypress', '*'], ['%', 'get_keypress', '%'], ['^2', 'get_keypress', '**2']],
    3: [['1', 'get_keypress', '1'], ['2', 'get_keypress', '2'], ['3', 'get_keypress', '3'],
        ['-', 'get_keypress', '-'], ['exp', 'get_keypress', '**'], ['pi', 'get_keypress', '*3.1416']],
    4: [['0', 'get_keypress', '0'], ['.', 'get_keypress', '.'], ['=', 'calculate', ''],
        ['+', 'get_keypress', '+'], ['(', 'get_keypress', '('], [')', 'get_keypress', ')']],
}

# loop through the list and create the calculator buttons
for keyRow in calcButtons:
    keyCol = 0
    for colVars in calcButtons[keyRow]:
        cmdFunction = eval(colVars[1])
        cButton = Button(mainWindow, text=colVars[0], padx=4)
        cButton.grid(row=keyRow, column=keyCol, sticky='nswe')
        cButton.config(command=partial(cmdFunction, colVars[2]))
        keyCol += 1

# grab the total window width and height and set minimum size
# (so buttons do not disappear if window is shrunk by user)
mainWindow.update()
windowWidth = mainWindow.winfo_width()
windowHeight = mainWindow.winfo_height()
mainWindow.minsize(windowWidth, windowHeight)

if __name__ == "__main__":
    mainWindow.mainloop()
