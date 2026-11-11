import tkinter as tk


# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")


# Display
display = tk.Entry(
    root,
    font=("Arial", 28),
    justify="right",
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    bd=0
)

display.pack(
    padx=15,
    pady=20,
    fill="x",
    ipady=15
)


# Button click function
def button_click(value):
    display.insert(tk.END, value)


# Clear function
def clear():
    display.delete(0, tk.END)


# Calculate function
def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# Buttons
buttons = [
    ["C", "/", "*", "←"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "(", ")"]
]


# Create buttons
for row in buttons:

    frame = tk.Frame(
        root,
        bg="#1e1e1e"
    )

    frame.pack(expand=True, fill="both")

    for button_text in row:

        if button_text == "C":
            command = clear

        elif button_text == "=":
            command = calculate

        elif button_text == "←":
            command = lambda: display.delete(
                len(display.get()) - 1,
                tk.END
            )

        else:
            command = lambda value=button_text: button_click(value)

        button = tk.Button(
            frame,
            text=button_text,
            font=("Arial", 18, "bold"),
            bg="#333333",
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            bd=0,
            command=command
        )

        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=3,
            pady=3
        )


root.mainloop()