import tkinter as tk
import random

class Minesweeper:
    def __init__(self, root, rows, cols, mines):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.buttons = [[None for _ in range(cols)] for _ in range(rows)]
        self.mine_positions = set()
        self.create_widgets()
        self.place_mines()
        self.calculate_numbers()

    def create_widgets(self):
        for r in range(self.rows):
            for c in range(self.cols):
                button = tk.Button(self.root, width=2, height=1, command=lambda r=r, c=c: self.reveal(r, c))
                button.bind("<Button-3>", lambda e, r=r, c=c: self.toggle_flag(r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button

    def place_mines(self):
        while len(self.mine_positions) < self.mines:
            r = random.randint(0, self.rows - 1)
            c = random.randint(0, self.cols - 1)
            self.mine_positions.add((r, c))

    def calculate_numbers(self):
        self.numbers = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for r, c in self.mine_positions:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and (nr, nc) not in self.mine_positions:
                        self.numbers[nr][nc] += 1

    def reveal(self, r, c):
        if (r, c) in self.mine_positions:
            self.buttons[r][c].config(text='*', background='red')
            self.game_over()
        else:
            self.buttons[r][c].config(text=self.numbers[r][c] if self.numbers[r][c] > 0 else '', relief=tk.SUNKEN, state=tk.DISABLED)

    def toggle_flag(self, r, c):
        current_text = self.buttons[r][c].cget('text')
        if current_text == '':
            self.buttons[r][c].config(text='F')
        elif current_text == 'F':
            self.buttons[r][c].config(text='')

    def game_over(self):
        for r, c in self.mine_positions:
            self.buttons[r][c].config(text='*', background='red')
        print("Game Over!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Minesweeper")
    game = Minesweeper(root, 10, 10, 10)  # 10x10 grid with 10 mines
    root.mainloop()
