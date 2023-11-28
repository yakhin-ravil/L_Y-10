# Крестики-нолики

from tkinter import *
import random

def stop_game():
    global game_left
    for item in game_left:
        buttons[item].config(bg="white", state="disabled")

def restart_game(): # Функция перезапуска игры
    global game, game_left, turn
    game = [None]*9
    game_left = list(range(9))
    turn = 0
    for i in range(9):
        buttons[i].config(text='', bg="purple", state="normal")
    label['text'] = "Крестики-нолики"

def win(n): # Определение выигрыша
    global game
    patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for p in patterns:
        if all(game[i] == n for i in p):
            return True

def push(b): # Процесс игры
    global game
    global game_left
    global turn
    game[b] = 'X'
    buttons[b].config(text='X', bg="white", state="disabled")
    game_left.remove(b)
    if b == 4 and turn == 0: # Если нажали на центральную кнопку на первом ходу
        t = random.choice(game_left) # Ход компьютера
    elif b != 4 and turn == 0:
        t = 4
    if turn > 0:
        t = 8 - b
    if t not in game_left:
        try:
            t = random.choice(game_left)
        except IndexError:
            label['text'] = 'Игра окончена!'
            stop_game()
    game[t] = '0'
    buttons[t].config(text='0', bg="white", state="disabled")
    if win('X'):
        label['text'] = 'Вы победили!'
        stop_game()
    elif win('0'):
        label['text'] = 'Вы проиграли!'
        stop_game()
    else:
        if (len(game_left) > 1):
            game_left.remove(t)
        else:
            label['text'] = 'Ничья!'
            stop_game()  # Вызываем функцию остановки игры, когда произошла ничья

game = [None]*9
game_left = list(range(9))
turn = 0

root = Tk()
label = Label(width=20, text="Крестики-нолики", font=('Arial', 20, 'bold'))

buttons = [Button(width=5, height=2, font=('Helvetica', 28, 'bold'), bg="purple", command=lambda x=i: push(x)) for i in range(9)]

label.grid(row=0, column=0, columnspan=3)

row = 1; col = 0
for i in range(9): # Распологаем кнопки
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

restart_button = Button(text="Начать заново", command=restart_game)  # Кнопка перезапуска игры
restart_button.grid(row=row + 1, column=0, columnspan=3)  

root.mainloop()