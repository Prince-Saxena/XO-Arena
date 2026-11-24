
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("420x600")
        self.root.resizable(True, True)
        self.root.minsize(380, 550)
        self.root.configure(bg="#111827")

        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        self.scores = {"X": 0, "O": 0, "Draw": 0}

        tk.Label(
            root,
            text="TIC TAC TOE",
            font=("Arial", 25, "bold"),
            bg="#111827",
            fg="#F9FAFB"
        ).pack(pady=(20, 5))

        self.status = tk.Label(
            root,
            text="Player X's Turn",
            font=("Arial", 14),
            bg="#111827",
            fg="#38BDF8"
        )
        self.status.pack(pady=10)

        self.score_label = tk.Label(
            root,
            text="X: 0     O: 0     Draws: 0",
            font=("Arial", 12),
            bg="#111827",
            fg="#D1D5DB"
        )
        self.score_label.pack(pady=5)

        self.frame = tk.Frame(root, bg="#374151")
        self.frame.pack(pady=20)

        self.buttons = []

        for i in range(9):
            button = tk.Button(
                self.frame,
                text="",
                font=("Arial", 28, "bold"),
                width=5,
                height=2,
                bg="#1F2937",
                fg="#F9FAFB",
                activebackground="#374151",
                relief="flat",
                command=lambda index=i: self.make_move(index)
            )
            button.grid(
                row=i // 3,
                column=i % 3,
                padx=3,
                pady=3
            )
            self.buttons.append(button)

        tk.Button(
            root,
            text="Restart Round",
            font=("Arial", 12, "bold"),
            bg="#2563EB",
            fg="white",
            activebackground="#1D4ED8",
            relief="flat",
            width=20,
            pady=10,
            command=self.restart_round
        ).pack(pady=8)

        tk.Button(
            root,
            text="New Game",
            font=("Arial", 11),
            bg="#374151",
            fg="white",
            relief="flat",
            width=20,
            pady=8,
            command=self.new_game
        ).pack(pady=5)

    def make_move(self, index):
        if self.board[index] != "" or self.game_over:
            return

        self.board[index] = self.current_player

        color = "#38BDF8" if self.current_player == "X" else "#FBBF24"

        self.buttons[index].config(
            text=self.current_player,
            fg=color,
            disabledforeground=color,
            state="disabled"
        )

        if self.check_winner():
            self.status.config(
                text=f"Player {self.current_player} Wins!",
                fg="#4ADE80"
            )
            self.scores[self.current_player] += 1
            self.game_over = True
            self.update_score()
            return

        if "" not in self.board:
            self.status.config(text="It's a Draw!", fg="#FBBF24")
            self.scores["Draw"] += 1
            self.game_over = True
            self.update_score()
            return

        self.current_player = "O" if self.current_player == "X" else "X"

        self.status.config(
            text=f"Player {self.current_player}'s Turn",
            fg="#38BDF8"
        )

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in winning_combinations:
            if (
                self.board[a] == self.board[b] == self.board[c]
                and self.board[a] != ""
            ):
                for index in (a, b, c):
                    self.buttons[index].config(bg="#166534")
                return True

        return False

    def update_score(self):
        self.score_label.config(
            text=f"X: {self.scores['X']}     "
                 f"O: {self.scores['O']}     "
                 f"Draws: {self.scores['Draw']}"
        )

    def restart_round(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False

        for button in self.buttons:
            button.config(
                text="",
                state="normal",
                bg="#1F2937"
            )

        self.status.config(
            text="Player X's Turn",
            fg="#38BDF8"
        )

    def new_game(self):
        self.scores = {"X": 0, "O": 0, "Draw": 0}
        self.update_score()
        self.restart_round()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
