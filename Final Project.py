import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice(): #Pick a random choice
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer): #compare the two answer
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def play_round(user_choice): #the actual game
    global user_score, computer_score
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)

    if result == "user":
        user_score += 1
        outcome = "You win this round!"
    elif result == "computer":
        computer_score += 1
        outcome = "Computer wins this round!"
    else:
        outcome = "It's a tie!"

    scoreboard.set(f"You: {user_score} | Computer: {computer_score}")
    messagebox.showinfo("Round Result", f"Computer chose: {computer_choice.capitalize()}\n{outcome}")

def reset_game(): #reset the scores
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    scoreboard.set("You: 0 | Computer: 0")

def create_ui(): #the actual thing to play the actual game and also ui
    global scoreboard

    root = tk.Tk()
    root.title("Rock Paper Scissors")

    tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack()

    tk.Button(button_frame, text="Rock", font=("Arial", 12), command=lambda: play_round("rock")).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Paper", font=("Arial", 12), command=lambda: play_round("paper")).pack(side=tk.LEFT, padx=5)
    tk.Button(button_frame, text="Scissors", font=("Arial", 12), command=lambda: play_round("scissors")).pack(side=tk.LEFT, padx=5)

    tk.Label(root, text="Scoreboard:", font=("Arial", 14)).pack(pady=10)

    scoreboard = tk.StringVar()
    scoreboard.set("You: 0 | Computer: 0")
    tk.Label(root, textvariable=scoreboard, font=("Arial", 14)).pack(pady=5)

    tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game).pack(pady=10)
    tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit).pack(pady=5)

    root.mainloop()

user_score = 0
computer_score = 0
create_ui()
