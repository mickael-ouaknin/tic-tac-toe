import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text='', command=lambda i=i, j=j: self.click(i, j), height=3, width=6)
                button.grid(row=i, column=j)
                self.board[i*3+j] = button

        self.window.mainloop()

    def click(self, i, j):
        if self.board[i*3+j]['text'] == '':
            self.board[i*3+j]['text'] = self.current_player
            if self.check_win(self.current_player):
                messagebox.showinfo("Gagné!", "Le joueur '" + self.current_player + "' a gagné!")
                self.window.destroy()
            elif '' not in [self.board[i]['text'] for i in range(9)]:
                messagebox.showinfo("Match nul!", "C'est un match nul!")
                self.window.destroy()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':
                    self.ia()

    def check_win(self, player):
        board = [self.board[i]['text'] for i in range(9)]
        winning_combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(board[i]==board[j]==board[k]==player for i,j,k in winning_combinations)

    def ia(self):
        empty_cells = [i for i in range(9) if self.board[i]['text'] == '']
        if empty_cells:
            cell = random.choice(empty_cells)
            self.board[cell]['text'] = 'O'
            if self.check_win('O'):
                messagebox.showinfo("Gagné!", "L'IA a gagné!")
                self.window.destroy()
            elif '' not in [self.board[i]['text'] for i in range(9)]:
                messagebox.showinfo("Match nul!", "C'est un match nul!")
                self.window.destroy()
            else:
                self.current_player = 'X'

if __name__ == "__main__":
    TicTacToe()