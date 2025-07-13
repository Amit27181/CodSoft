import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Emoji map
emoji_map = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("420x480")
root.resizable(False, False)
root.config(bg="#f0f8ff")

# Game logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_display.config(text=f"You chose: {emoji_map[user_choice]} {user_choice}")
    computer_display.config(text=f"Computer chose: {emoji_map[computer_choice]} {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "Computer Wins! 🤖"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Let's play Rock-Paper-Scissors!")
    score_label.config(text="Score → You: 0 | Computer: 0")
    user_display.config(text="")
    computer_display.config(text="")

# Title
tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 22, "bold"), bg="#f0f8ff", fg="#333").pack(pady=15)

# User and computer choice display
user_display = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
user_display.pack()

computer_display = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
computer_display.pack()

# Result label
result_label = tk.Label(root, text="Let's play Rock-Paper-Scissors!", font=("Arial", 14, "italic"), bg="#f0f8ff", fg="#444")
result_label.pack(pady=10)

# Button frame
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=15)

# Colorful buttons
rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 12, "bold"), width=10,
                     bg="#ff9999", fg="white", activebackground="#ff4d4d", command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12, "bold"), width=10,
                      bg="#99ccff", fg="white", activebackground="#3399ff", command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 12, "bold"), width=10,
                         bg="#99ff99", fg="white", activebackground="#33cc33", command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Score display
score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 14), bg="#f0f8ff", fg="#222")
score_label.pack(pady=15)

# Reset button
tk.Button(root, text="🔁 Reset Game", font=("Arial", 12, "bold"), bg="#cccccc", fg="black",
          activebackground="#999999", command=reset_game).pack(pady=10)

# Start the GUI loop
root.mainloop()
import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Emoji map
emoji_map = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("420x480")
root.resizable(False, False)
root.config(bg="#f0f8ff")

# Game logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_display.config(text=f"You chose: {emoji_map[user_choice]} {user_choice}")
    computer_display.config(text=f"Computer chose: {emoji_map[computer_choice]} {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "Computer Wins! 🤖"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Let's play Rock-Paper-Scissors!")
    score_label.config(text="Score → You: 0 | Computer: 0")
    user_display.config(text="")
    computer_display.config(text="")

# Title
tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 22, "bold"), bg="#f0f8ff", fg="#333").pack(pady=15)

# User and computer choice display
user_display = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
user_display.pack()

computer_display = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff")
computer_display.pack()

# Result label
result_label = tk.Label(root, text="Let's play Rock-Paper-Scissors!", font=("Arial", 14, "italic"), bg="#f0f8ff", fg="#444")
result_label.pack(pady=10)

# Button frame
button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=15)

# Colorful buttons
rock_btn = tk.Button(button_frame, text="🪨 Rock", font=("Arial", 12, "bold"), width=10,
                     bg="#ff9999", fg="white", activebackground="#ff4d4d", command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="📄 Paper", font=("Arial", 12, "bold"), width=10,
                      bg="#99ccff", fg="white", activebackground="#3399ff", command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="✂️ Scissors", font=("Arial", 12, "bold"), width=10,
                         bg="#99ff99", fg="white", activebackground="#33cc33", command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

# Score display
score_label = tk.Label(root, text="Score → You: 0 | Computer: 0", font=("Arial", 14), bg="#f0f8ff", fg="#222")
score_label.pack(pady=15)

# Reset button
tk.Button(root, text="🔁 Reset Game", font=("Arial", 12, "bold"), bg="#cccccc", fg="black",
          activebackground="#999999", command=reset_game).pack(pady=10)

# Start the GUI loop
root.mainloop()
