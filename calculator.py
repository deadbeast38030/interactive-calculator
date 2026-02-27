import tkinter as tk
from tkinter import messagebox

# Track which entry is active
active_entry = None


def set_active_entry(entry):
    global active_entry
    active_entry = entry


def add():
    calculate(lambda n1, n2: n1 + n2)


def sub():
    calculate(lambda n1, n2: n1 - n2)


def mul():
    calculate(lambda n1, n2: n1 * n2)


def dev():
    def division(n1, n2):
        if n2 == 0:
            messagebox.showerror("Error", "Cannot divide by zero.")
            return None
        return n1 / n2

    calculate(division)


def calculate(operation):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        result_value = operation(n1, n2)

        if result_value is not None:
            result.config(text=f"Result: {result_value:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    result.config(text="Result: ")


def add_to_entry(value):
    if active_entry is not None:
        active_entry.insert(tk.END, value)


# ------------------- MAIN WINDOW -------------------

root = tk.Tk()
root.title("Interactive Calculator")
root.geometry("350x500")
root.configure(bg="black")

# ------------------- ENTRY 1 -------------------

label1 = tk.Label(root, text="Enter first number:", bg="black", fg="white")
label1.pack(pady=5)

entry1 = tk.Entry(root, width=20)
entry1.pack(pady=5)
entry1.bind("<FocusIn>", lambda event: set_active_entry(entry1))

# ------------------- ENTRY 2 -------------------

label2 = tk.Label(root, text="Enter second number:", bg="black", fg="white")
label2.pack(pady=5)

entry2 = tk.Entry(root, width=20)
entry2.pack(pady=5)
entry2.bind("<FocusIn>", lambda event: set_active_entry(entry2))

# ------------------- OPERATION BUTTONS -------------------

button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=15)

add_button = tk.Button(button_frame, text="+", width=5, bg="orange", command=add)
add_button.grid(row=0, column=0, padx=5)

sub_button = tk.Button(button_frame, text="-", width=5, bg="orange", command=sub)
sub_button.grid(row=0, column=1, padx=5)

mul_button = tk.Button(button_frame, text="*", width=5, bg="orange", command=mul)
mul_button.grid(row=0, column=2, padx=5)

dev_button = tk.Button(button_frame, text="/", width=5, bg="orange", command=dev)
dev_button.grid(row=0, column=3, padx=5)

# ------------------- RESULT -------------------

result = tk.Label(root, text="Result: ", bg="black", fg="light green", font=("Arial", 12))
result.pack(pady=15)

# ------------------- NUMBER BUTTONS -------------------

number_frame = tk.Frame(root, bg="black")
number_frame.pack()

for i in range(1, 10):
    button = tk.Button(
        number_frame,
        text=str(i),
        width=5,
        bg="grey",
        command=lambda i=i: add_to_entry(str(i))
    )
    button.grid(row=(i - 1) // 3, column=(i - 1) % 3, padx=5, pady=5)

# Zero button
zero_button = tk.Button(
    number_frame,
    text="0",
    width=5,
    bg="grey",
    command=lambda: add_to_entry("0")
)
zero_button.grid(row=3, column=1, padx=5, pady=5)

# Clear button
clear_button = tk.Button(
    number_frame,
    text="Clear",
    width=5,
    bg="red",
    command=clear
)
clear_button.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()