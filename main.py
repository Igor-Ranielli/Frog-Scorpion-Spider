import tkinter
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

import random

# cores --------------------------------
white = "#FFFFFF"  
gray = "#333333"  
orange = "#fcc058"  
yellow = "#fff873"  
green = "#34eb3d"   
red = "#e85151"    
background = "#3b3b3b"

#configuração da janela
window = Tk()
window.title('')
window.geometry('260x280')
window.configure(bg=background)

# parte de cima da janela

frame_up = Frame(window, width=260, height=100, bg=gray, relief='raised')
frame_up.grid(row = 0, column = 0, sticky=NW)

# parte de baixo da janela

frame_down = Frame(window, width=260, height=300, bg=white, relief='flat')
frame_down.grid(row = 1, column = 0, sticky=NW)

style = ttk.Style(window)
style .theme_use('clam')

# configurando o frame cima, app 1 = jogador 1 / app 2 = cpu

app_1 = Label(frame_up, text="You", height=1, anchor='center', font=('Ivy 10 bold'), bg=gray, fg=white)
app_1.place(x=25, y=70)
app_1_line = Label(frame_up, height=10, anchor='center', font=('Ivy 10 bold'), bg=white, fg=white)
app_1_line.place(x=0, y=0)
app_1_points = Label(frame_up, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=gray, fg=white)
app_1_points.place(x=50, y=20)

app_ = Label(frame_up, text=":", height=1, anchor='center', font=('Ivy 30 bold'), bg=gray, fg=white)
app_.place(x=115, y=20)

app_2_points = Label(frame_up, text="0", height=1, anchor='center', font=('Ivy 30 bold'), bg=gray, fg=white)
app_2_points.place(x=170, y=20)
app_2 = Label(frame_up, text="CPU", height=1, anchor='center', font=('Ivy 10 bold'), bg=gray, fg=white)
app_2.place(x=205, y=70)
app_2_line = Label(frame_up, height=10, anchor='center', font=('Ivy 10 bold'), bg=white, fg=white)
app_2_line.place(x=255, y=0)

app_line = Label(frame_up, width=255, anchor='center', font=('Ivy 1 bold'), bg=yellow, fg=white)
app_line.place(x=0, y=95)


b_play = Button(frame_down, command=play_game, width=30, text='Play', bg=background, fg=white, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_play.place(x=5, y=135)

window.mainloop()