import tkinter as tk
from tkinter import messagebox


# Main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")


# Game variables
current_player = "X"
buttons = []
game_over = False


# Winning combinations
winning_combinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def check_winner():
    for a, b, c in winning_combinations:

        if (
            buttons[a]["text"] != ""
            and buttons[a]["text"]
            == buttons[b]["text"]
            == buttons[c]["text"]
        ):
            # Winning buttons ko highlight karo
            buttons[a].config(bg="#00c853")
            buttons[b].config(bg="#00c853")
            buttons[c].config(bg="#00c853")

            return True

    return False


def check_draw():
    for button in buttons:
        if button["text"] == "":
            return False

    return True


def button_click(index):
    global current_player, game_over

    # Agar game khatam ho gaya hai
    if game_over:
        return

    # Agar button already selected hai
    if buttons[index]["text"] != "":
        return

    # Player ka symbol lagao
    buttons[index]["text"] = current_player

    # X aur O ke different colors
    if current_player == "X":
        buttons[index].config(fg="#ff5252")
    else:
        buttons[index].config(fg="#40c4ff")

    # Winner check
    if check_winner():
        game_over = True
        status_label.config(
            text=f"🎉 Player {current_player} Wins!",
            fg="#00c853"
        )
        return

    # Draw check
    if check_draw():
        game_over = True
        status_label.config(
            text="🤝 It's a Draw!",
            fg="#ffd740"
        )
        return

    # Player change
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    status_label.config(
        text=f"Player {current_player}'s Turn"
    )


def restart_game():
    global current_player, game_over

    current_player = "X"
    game_over = False

    for button in buttons:
        button.config(
            text="",
            bg="#2d2d2d",
            fg="white"
        )

    status_label.config(
        text="Player X's Turn",
        fg="white"
    )


# Title
title_label = tk.Label(
    root,
    text="TIC-TAC-TOE",
    font=("Arial", 28, "bold"),
    bg="#1e1e1e",
    fg="white"
)

title_label.pack(pady=20)


# Status
status_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
)

status_label.pack(pady=10)


# Game board
board_frame = tk.Frame(
    root,
    bg="#1e1e1e"
)

board_frame.pack(pady=10)


# Create 9 buttons
for i in range(9):

    button = tk.Button(
        board_frame,
        text="",
        font=("Arial", 32, "bold"),
        width=4,
        height=2,
        bg="#2d2d2d",
        fg="white",
        activebackground="#444444",
        activeforeground="white",
        relief="flat",
        command=lambda i=i: button_click(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=5,
        pady=5
    )

    buttons.append(button)


# Restart button
restart_button = tk.Button(
    root,
    text="🔄 Restart Game",
    font=("Arial", 14, "bold"),
    bg="#6200ee",
    fg="white",
    activebackground="#7c4dff",
    activeforeground="white",
    relief="flat",
    padx=20,
    pady=10,
    command=restart_game
)

restart_button.pack(pady=20)


# Start game
root.mainloop()

