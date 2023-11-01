import tkinter as tk
from tkinter import messagebox, simpledialog


def iswin(board):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for combination in winning_combinations:
        i, j, k = combination[0], combination[1], combination[2]
        if board[i] == board[j] and board[i] == board[k]:
            if board[i] != " ":
                return board[i]


def draw(board):
    return not " " in board


def utility(player, board):
    win = iswin(board)
    if win:
        if win == player:
            return 1
        else:
            return -1
    return 0


def opponent(player):
    if player == "X":
        return "O"
    return "X"


def available_move(board):
    lst = []
    for i in range(len(board)):
        if board[i] == " ":
            lst.append(i)
    return lst


def minimax(board, current_player, max_player="O"):
    if iswin(board):
        if iswin(board) == max_player:
            return 1, None
        else:
            return -1, None

    if draw(board):
        return 0, None

    moves = available_move(board)

    if current_player == max_player:
        best_move = None
        best_utility = float("-inf")
        for move in moves:
            new_board = board.copy()
            new_board[move] = current_player
            new_utility, _ = minimax(new_board, opponent(current_player),
                                     max_player)

            if new_utility > best_utility:
                best_utility = new_utility
                best_move = move
        return best_utility, best_move

    else:
        best_move = None
        best_utility = float("inf")
        for move in moves:
            new_board = board.copy()
            new_board[move] = current_player
            new_utility, _ = minimax(new_board, opponent(current_player),
                                     max_player)

            if new_utility < best_utility:
                best_utility = new_utility
                best_move = move
        return best_utility, best_move


class TicTacToeGUI:
    def __init__(self):
        self.p1 = "A"
        self.p2 = "A"
        self.current_player = "X"
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe GUI")

        # Initialize board
        self.board = [" " for _ in range(9)]

        # Create buttons
        self.buttons = [
            tk.Button(self.root, text=" ", font="Arial 20", width=5, height=2,
                      command=lambda i=i: self.make_move(i)) for i in range(9)]

        # Position buttons
        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col)

        self.choose_mode()

        self.root.mainloop()

    def choose_mode(self):
        self.mode_window = tk.Toplevel(self.root)
        self.mode_window.title("Choose Mode")

        self.mode_var = tk.StringVar()
        self.mode_var.set("1")  # default value

        modes = [
            ("Player vs Player", "1"),
            ("Player vs AI", "2"),
            ("AI vs Player", "3"),
            ("AI vs AI", "4")
        ]

        for text, mode in modes:
            radiobutton = tk.Radiobutton(self.mode_window, text=text, variable=self.mode_var, value=mode)
            radiobutton.pack(anchor="w")

        confirm_button = tk.Button(self.mode_window, text="Confirm", command=self.set_mode)
        confirm_button.pack(pady=10)

    def set_mode(self):
        choice = self.mode_var.get()
        if choice == "1":
            self.p1 = "H"
            self.p2 = "H"
        elif choice == "2":
            self.p1 = "H"
            self.p2 = "A"
        elif choice == "3":
            self.p1 = "A"
            self.p2 = "H"
        elif choice == "4":
            self.p1 = "A"
            self.p2 = "A"

        self.mode_window.destroy()
        if self.p1 == "A":
            self.ai_move()

    def make_move(self, position):
        if self.board[position] == " ":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player)
            winner = iswin(self.board)
            if winner:
                self.end_game(winner)
                return
            elif draw(self.board):
                self.end_game(None)
                return

            self.current_player = opponent(self.current_player)

            # Check if next player is AI
            if (self.current_player == "X" and self.p1 == "A") or (
                    self.current_player == "O" and self.p2 == "A"):
                self.ai_move()

    def ai_move(self):
        self.root.after(1000, self.execute_ai_move)

    def execute_ai_move(self):
        move = minimax(self.board, self.current_player)[1]
        self.make_move(move)

    def end_game(self, winner):
        if winner:
            messagebox.showinfo("Game Over", f"{winner} Wins!")
        else:
            messagebox.showinfo("Game Over", "It's a Draw!")

        # Reset game
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.choose_mode()


if __name__ == "__main__":
    TicTacToeGUI()
