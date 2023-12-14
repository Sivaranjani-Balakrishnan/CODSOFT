import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#808080") 

        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.max_rounds = 0

        self.label_game_name = tk.Label(self.root, text="ROCK PAPER SCISSORS", font=("Arial", 24, "bold"), bg="#808080", fg="black")  
        self.label_game_name.pack(pady=(20, 10))  

        self.label_instruction = tk.Label(self.root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14), bg="#808080", fg="blue")  
        self.label_instruction.pack(pady=10)

        self.label_rounds = tk.Label(self.root, text="Number of Rounds: ", font=("Arial", 14), bg="#808080", fg="black")  
        self.label_rounds.pack(pady=10)

        self.entry_rounds = tk.Entry(self.root, font=("Arial", 14), bd=5, relief=tk.GROOVE)
        self.entry_rounds.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root, bg="#808080")
        self.buttons_frame.pack()

        choices = ['Rock', 'Paper', 'Scissors']

        for choice in choices:
            button = tk.Button(self.buttons_frame, text=choice, font=("Arial", 12), padx=20, pady=10, bg="aqua", fg="black", command=lambda c=choice: self.play_round(c))  
            button.pack(side=tk.LEFT, padx=10)

        self.label_result = tk.Label(self.root, text="", font=("Arial", 14), bg="#808080", fg="black")  
        self.label_result.pack(pady=10)

        self.label_score = tk.Label(self.root, text=f"Score: User {self.user_score} - {self.computer_score} Computer", font=("Arial", 14), bg="#808080", fg="black")  
        self.label_score.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", font=("Arial", 14), bg="aqua", padx=20, pady=10, command=self.reset_game, fg="black")  
        self.play_again_button.pack(pady=10)
        self.play_again_button.pack_forget()

    def play_round(self, user_choice):
        try:
            if self.rounds_played == 0:
                self.max_rounds = int(self.entry_rounds.get())
                self.label_rounds.config(text=f"Number of Rounds: {self.max_rounds}")

            computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

            result = self.determine_winner(user_choice, computer_choice)

            self.label_result.config(text=f"User: {user_choice}   Computer: {computer_choice}\nResult: {result}", fg=self.get_result_color(result))

            if result == "Win":
                self.user_score += 1
            elif result == "Lose":
                self.computer_score += 1

            self.rounds_played += 1
            self.label_score.config(text=f"Score: User {self.user_score} - {self.computer_score} Computer")

            if self.rounds_played == self.max_rounds:
                self.end_game()
            else:
                self.play_again_button.pack()

        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number of rounds.")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Scissors" and computer_choice == "Paper") or
            (user_choice == "Paper" and computer_choice == "Rock")
        ):
            return "Win"
        else:
            return "Lose"

    def get_result_color(self, result):
        if result == "Win":
            return "green"
        elif result == "Lose":
            return "red"
        else:
            return "orange"

    def end_game(self):
        winner = "User" if self.user_score > self.computer_score else "Computer" if self.computer_score > self.user_score else "Tie"
        messagebox.showinfo("Game Over", f"Game Over!\nFinal Score: User {self.user_score} - {self.computer_score} Computer\nWinner: {winner}")
        self.play_again_button.pack()  

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.max_rounds = 0
        self.label_result.config(text="")
        self.label_score.config(text=f"Score: User {self.user_score} - {self.computer_score} Computer")
        self.play_again_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
