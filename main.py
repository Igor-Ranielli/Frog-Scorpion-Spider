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

app_line = Label(frame_up, width=255, anchor='center', font=('Ivy 1 bold'), bg=white, fg=white)
app_line.place(x=0, y=95)

app_cpu = Label(frame_down, text="", height=1, anchor='center', font=('Ivy 10 bold'), bg=white, fg=white)
app_cpu.place(x=190, y=10)

global you
global cpu
global rounds
global points_you
global points_cpu

points_you = 0
points_cpu = 0
rounds = 5

# Função lógica do jogo
def play(i):
    global rounds
    global points_you
    global points_cpu

    if rounds >0:
        options = ['Frog', 'Scorpion', 'Spider']
        cpu = random.choice(options)
        you = i
        app_cpu['text'] = cpu
        app_cpu['fg'] = gray

        # Condições para o jogo ter um vencedor
        if you == 'Frog' and cpu == 'Frog' or you == 'Scorpion' and cpu == 'Scorpion' or you == 'Spider' and cpu == 'Spider':
            print('Os mesmos animais foram escolhidos e ocorreu um empate')
            app_line['bg'] = "yellow"
            app_1_line['bg'] = "white"
            app_2_line['bg'] = "white"

        elif you == 'Frog' and cpu == 'Scorpion':
            print('O escorpião matou o sapo com o seu ferrão, você perdeu.')
            app_line['bg'] = "white"
            app_1_line['bg'] = "red"
            app_2_line['bg'] = "green"
            points_cpu += 1
        
        elif you == 'Frog' and cpu == 'Spider':
            print('O sapo engoliu a aranha com sua lingua, você ganhou.')
            app_line['bg'] = "white"
            app_1_line['bg'] = "green"
            app_2_line['bg'] = "red"
            points_you += 1
        
        elif you == 'Scorpion' and cpu == 'Frog':
            print('O escorpião matou o sapo com o seu ferrão, você ganhou.')
            app_line['bg'] = "white"
            app_1_line['bg'] = "green"
            app_2_line['bg'] = "red"
            points_you += 1
        
        elif you == 'Scorpion' and cpu == 'Spider':
            print('A aranha enrolou o escorpião em sua teia, você perdeu.')
            app_line['bg'] = "white"
            app_1_line['bg'] = "red"
            app_2_line['bg'] = "green"
            points_cpu += 1

        elif you == 'Spider' and cpu == 'Frog':
            print('O sapo engoliu a aranha com sua lingua, você perdeu.')
            app_line['bg'] = "white"
            app_1_line['bg'] = "red"
            app_2_line['bg'] = "green"
            points_cpu += 1

        elif you == 'Spider' and cpu == 'Scorpion':
            print('A aranha enrolou o escorpião em sua teia, você ganhou.')
            app_line['bg'] = "white"
            app_1_line['bg'] = "green"
            app_2_line['bg'] = "red"
            points_you += 1
        
        # Atualizando a pontuação
        app_1_points['text'] = points_you
        app_2_points['text'] = points_cpu

        # Atualizando o número de rounds
        rounds -= 1

        
        


    else:
        app_1_points['text'] = points_you
        app_2_points['text'] = points_cpu
        end_game()

# Função iniciar o jogo
def play_game():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_play.destroy()

    icon_1 = Image.open('Images/frog.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_down, command=lambda: play('Frog'), width=50, image=icon_1, compound=CENTER, bg=white, fg=white, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('Images/scorpion.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_down, command=lambda: play('Scorpion'), width=50, image=icon_2, compound=CENTER, bg=white, fg=white, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_2.place(x=100, y=60)

    icon_3 = Image.open('Images/spider.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_down, command=lambda: play('Spider'), width=50, image=icon_3, compound=CENTER, bg=white, fg=white, font=('Ivy 10 bold'), anchor=CENTER, relief=FLAT)
    b_icon_3.place(x=190, y=60)

# Função terminar o jogo
def end_game():
    global rounds
    global points_you
    global points_cpu
    
    # reiniciando as variáveis para zero
    points_cpu = 0
    points_you = 0
    rounds = 5

    # destruindo os botões de jogo
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    # definindo o vencedor
    player_you = int(app_1_points['text'])
    player_cpu = int(app_2_points['text'])

    if player_you > player_cpu:
        app_winner = Label(frame_down, text="Você venceu!", height=1, anchor='center', font=('Ivy 10 bold'), bg=white, fg=green)
        app_winner.place(x=5, y=60)
        app_line['bg'] = "green"
        app_1_line['bg'] = "green"
        app_2_line['bg'] = "green"
    elif player_you < player_cpu:
        app_winner = Label(frame_down, text="Você perdeu.", height=1, anchor='center', font=('Ivy 10 bold'), bg=white, fg=red)
        app_winner.place(x=5, y=60)
        app_line['bg'] = "red"
        app_1_line['bg'] = "red"
        app_2_line['bg'] = "red"
    else:
        app_winner = Label(frame_down, text="Você empatou.", height=1, anchor='center', font=('Ivy 10 bold'), bg=white, fg=yellow)
        app_winner.place(x=5, y=60)
        app_line['bg'] = "yellow"
        app_1_line['bg'] = "yellow"
        app_2_line['bg'] = "yellow"


    def play_again():
        app_1_points['text'] = '0'
        app_2_points['text'] = '0'
        app_winner.destroy()
        b_playAgain.destroy()

        play_game()
    b_playAgain = Button(frame_down, command=play_again, width=30, text='Play Again?', bg=background, fg=white, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    b_playAgain.place(x=5, y=135)



b_play = Button(frame_down, command=play_game, width=30, text='Play', bg=background, fg=white, font=('Ivy 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
b_play.place(x=5, y=135)

window.mainloop()