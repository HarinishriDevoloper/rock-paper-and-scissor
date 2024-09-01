import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Rock Paper Scissors")

player_score = 0
computer_score = 0
round_count = 0

def resize_image(image_path, size=(500, 300)):
    image = Image.open(image_path)
    image = image.resize(size)
    return ImageTk.PhotoImage(image)

rock_img = resize_image("images/rock.png" ,(200,200))
paper_img = resize_image("images/paper.png",(200,200))
scissors_img = resize_image("images/scissors.png",(200,200))

play_button_img = resize_image("images/button_lets-play-a-game.png", size=(150, 50))
start_button_img = resize_image("images/button_start-game.png", size=(150, 50))
try_again_button_img = resize_image("images/button_try-again.png", size=(150, 50))
cancel_button_img = resize_image("images/button_cancel.png", size=(150, 50))

computer_images = {
    "Rock": rock_img,
    "Paper": paper_img,
    "Scissors": scissors_img
}

def reset_game():
    global player_score, computer_score, round_count
    player_score = 0
    computer_score = 0
    round_count = 0
    result_window.destroy()
    start_game()

def start_game():
    start_frame.pack_forget()
    game_frame.pack()
    result_label.config(text="")
    choice_label.config(text=f"{player_name}, make your choice:")
    computer_choice_image_label.config(image='')
    computer_choice_label.config(text="")


def play_game(player_choice):
    global player_score, computer_score, round_count

    computer_choice = random.randint(0, 2)
    if player_choice == computer_choice:
        result = "It's a draw"
    elif (player_choice == 0 and computer_choice == 2) or \
         (player_choice == 1 and computer_choice == 0) or \
         (player_choice == 2 and computer_choice == 1):
        player_score += 1
    else:
        computer_score += 1

    round_count += 1
    
    computer_choice_text = choices[computer_choice]
    computer_choice_image_label.config(image=computer_images[computer_choice_text])
    computer_choice_label.config(text=f"Computer chose {computer_choice_text}")

    if round_count < 5:
        choice_label.config(text=f"Round {round_count}: Computer chose {choices[computer_choice]}")
        result_label.config(text=f"Player Score: {player_score} - Computer Score: {computer_score}")
    else:
        show_result_window()

def exit_game():
    root.quit()

def get_name():
    global player_name
    player_name = name_entry.get()
    if player_name:
        start_frame.pack()
        name_frame.pack_forget()
    else:
        messagebox.showerror("Error", "Please enter your name")

def start_main_game():
    welcome_frame.pack_forget()
    name_frame.pack(pady=20)

def show_result_window():
    global result_window
    result_window = tk.Toplevel(root)
    result_window.title("Game Over")

    if player_score > computer_score:
        result_text = f"Congratulations {player_name}, you win!"
        result_image=resize_image("images/congragulations.png")
       
    else:
        result_text = f"Sorry {player_name}, you lose. Better luck next time!"
        result_image=resize_image("images/games.png")
       
    result_label = tk.Label(result_window, text=result_text, font=("Arial", 14))
    result_label.pack(pady=10)
    result_image_label=tk.Label(result_window,image=result_image)
    result_image_label.image=result_image
    result_image_label.pack(pady=10)


    try_again_button = tk.Button(result_window, image=try_again_button_img, command=reset_game)
    try_again_button.pack(side=tk.LEFT, padx=10, pady=10)

    cancel_button = tk.Button(result_window, image=cancel_button_img, command=exit_game)
    cancel_button.pack(side=tk.RIGHT, padx=10, pady=10)


welcome_frame = tk.Frame(root)
welcome_frame.pack()

welcome_img = resize_image("images/imagess.png") 
welcome_label = tk.Label(welcome_frame, image=welcome_img)
welcome_label.pack(pady=20)

play_button = tk.Button(welcome_frame, image=play_button_img, command=start_main_game)
play_button.pack(pady=10)


name_frame = tk.Frame(root)
name_label = tk.Label(name_frame, text="Enter your name:")
name_label.pack(side=tk.LEFT)
name_entry = tk.Entry(name_frame)
name_entry.pack(side=tk.LEFT)
submit_name_button = tk.Button(name_frame, text="Submit", command=get_name)
submit_name_button.pack(side=tk.LEFT)


start_frame = tk.Frame(root)
game_start_img = resize_image("images/start image.png") 
game_start_label = tk.Label(start_frame, image=game_start_img)
game_start_label.pack(pady=20)

start_button = tk.Button(start_frame, image=start_button_img, command=start_game)
start_button.pack(pady=10)


game_frame = tk.Frame(root)
choices = ["Rock", "Paper", "Scissors"]

choice_label = tk.Label(game_frame, text="")
choice_label.pack(pady=10)

rock_button = tk.Button(game_frame, image=rock_img, command=lambda: play_game(0))
rock_button.pack(side=tk.LEFT, padx=5)
paper_button = tk.Button(game_frame, image=paper_img, command=lambda: play_game(1))
paper_button.pack(side=tk.LEFT, padx=5)
scissors_button = tk.Button(game_frame, image=scissors_img, command=lambda: play_game(2))
scissors_button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(game_frame, text="")
result_label.pack(pady=10)

computer_choice_image_label = tk.Label(game_frame)
computer_choice_image_label.pack(pady=5)

computer_choice_label = tk.Label(game_frame, text="")
computer_choice_label.pack(pady=5)

root.mainloop()