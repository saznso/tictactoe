import tkinter as tk
from tkinter import messagebox


def button_click(button):

    global clicked, count

    if button['text'] == ' ' and clicked == True:

        button['text'] = 'X'
        clicked = False
        count += 1

        if_won()

    elif button['text'] == ' ' and clicked == False:

        button['text'] = 'O'
        clicked = True
        count += 1

        if_won()

    else:

        messagebox.showerror('tic tac toe', 'occupied')

def disable_all():

    button1['state'] = 'disabled'
    button2['state'] = 'disabled'
    button3['state'] = 'disabled'
    button4['state'] = 'disabled'
    button5['state'] = 'disabled'
    button6['state'] = 'disabled'
    button7['state'] = 'disabled'
    button8['state'] = 'disabled'
    button9['state'] = 'disabled'

def reset():

    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '

    button1.config(highlightbackground = 'lavender')
    button2.config(highlightbackground = 'lavender')
    button3.config(highlightbackground = 'lavender')
    button4.config(highlightbackground = 'lavender')
    button5.config(highlightbackground = 'lavender')
    button6.config(highlightbackground = 'lavender')
    button7.config(highlightbackground = 'lavender')
    button8.config(highlightbackground = 'lavender')
    button9.config(highlightbackground = 'lavender')

    button1['state'] = 'normal'
    button2['state'] = 'normal'
    button3['state'] = 'normal'
    button4['state'] = 'normal'
    button5['state'] = 'normal'
    button6['state'] = 'normal'
    button7['state'] = 'normal'
    button8['state'] = 'normal'
    button9['state'] = 'normal'

def if_won():

    global winner
    winner = False

    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X':

        button1.config(highlightbackground = 'green')
        button2.config(highlightbackground = 'green')
        button3.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'X wins')

        disable_all()

    elif button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X':

        button4.config(highlightbackground = 'green')
        button5.config(highlightbackground = 'green')
        button6.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'X wins')

        disable_all()

    elif button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X':

        button7.config(highlightbackground = 'green')
        button8.config(highlightbackground = 'green')
        button9.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'X wins')

        disable_all()

    elif button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X':

        button1.config(highlightbackground = 'green')
        button4.config(highlightbackground = 'green')
        button7.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'X wins')

        disable_all()

    elif button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X':

        button2.config(highlightbackground = 'green')
        button5config(highlightbackground = 'green')
        button8.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'X wins')

        disable_all()

    elif button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X':

        button3.config(highlightbackground = 'green')
        button6.config(highlightbackground = 'green')
        button9.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'X wins')

        disable_all()

    elif button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X':

        button1.config(highlightbackground = 'green')
        button5.config(highlightbackground = 'green')
        button9.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'X wins')

        disable_all()
        
    elif button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':

        button3.config(highlightbackground = 'green')
        button5.config(highlightbackground = 'green')
        button7.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'X wins')

        disable_all()

    elif button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O':

        button1.config(highlightbackground = 'green')
        button2.config(highlightbackground = 'green')
        button3.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'O wins')

        disable_all()

    elif button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O':

        button4.config(highlightbackground = 'green')
        button5.config(highlightbackground = 'green')
        button6.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'O wins')

        disable_all()

    elif button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O':

        button7.config(highlightbackground = 'green')
        button8.config(highlightbackground = 'green')
        button9.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'O wins')

        disable_all()

    elif button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O':

        button1.config(highlightbackground = 'green')
        button4.config(highlightbackground = 'green')
        button7.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'O wins')

        disable_all()

    elif button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O':

        button2.config(highlightbackground = 'green')
        button5.config(highlightbackground = 'green')
        button8.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'O wins')

        disable_all()

    elif button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O':

        button3.config(highlightbackground = 'green')
        button6.config(highlightbackground = 'green')
        button9.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'O wins')

        disable_all()

    elif button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O':

        button1.config(highlightbackground = 'green')
        button5.config(highlightbackground = 'green')
        button9.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'O wins')

        disable_all()
        
    elif button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O':

        button3.config(highlightbackground = 'green')
        button5.config(highlightbackground = 'green')
        button7.config(highlightbackground = 'green')
        winner = True
        messagebox.showinfo('tic tac toe', 'O wins')

        disable_all()
    
clicked = True
count = 0

window = tk.Tk()
window.title('tic tac toe')
window.config(bg = 'white')

frame = tk.Frame(window)
frame.config(bg = 'white')
frame.grid(column = 0, row = 0, padx = 20, pady = 20)

title = tk.Label(frame, text = 'tic tac toe')
title.config(fg = 'black', bg = 'lavender', font = ('calibri bold', 24), width = 10)
title.grid(column = 0, row = 0, columnspan = 3, padx = 5, pady = 15, sticky = 'ew')

button1 = tk.Button(frame, text = ' ', command = lambda:button_click(button1))
button1.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button1.grid(column = 0, row = 1, columnspan = 1, padx = 5, pady = 5)

button2 = tk.Button(frame, text = ' ', command = lambda:button_click(button2))
button2.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button2.grid(column = 1, row = 1, columnspan = 1, padx = 5, pady = 5)

button3 = tk.Button(frame, text = ' ', command = lambda:button_click(button3))
button3.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button3.grid(column = 2, row = 1, columnspan = 1, padx = 5, pady = 5)

button4 = tk.Button(frame, text = ' ', command = lambda:button_click(button4))
button4.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button4.grid(column = 0, row = 2, columnspan = 1, padx = 5, pady = 5)

button5 = tk.Button(frame, text = ' ', command = lambda:button_click(button5))
button5.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button5.grid(column = 1, row = 2, columnspan = 1, padx = 5, pady = 5)

button6 = tk.Button(frame, text = ' ', command = lambda:button_click(button6))
button6.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button6.grid(column = 2, row = 2, columnspan = 1, padx = 5, pady = 5)

button7 = tk.Button(frame, text = ' ', command = lambda:button_click(button7))
button7.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button7.grid(column = 0, row = 3, columnspan = 1, padx = 5, pady = 5)

button8 = tk.Button(frame, text = ' ', command = lambda:button_click(button8))
button8.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button8.grid(column = 1, row = 3, columnspan = 1, padx = 5, pady = 5)

button9 = tk.Button(frame, text = ' ', command = lambda:button_click(button9))
button9.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 3, height = 2)
button9.grid(column = 2, row = 3, columnspan = 1, padx = 5, pady = 5)

reset_button = tk.Button(frame, text = 'reset', command = reset)
reset_button.config(highlightbackground = 'lavender', fg = 'black', font = ('calibri bold', 24), width = 10)
reset_button.grid(column = 0, row = 4, columnspan = 3, padx = 5, pady = 15, sticky = 'ew')

