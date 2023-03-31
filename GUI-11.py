import tkinter as tk

def count_chars(*args):
    name = name_var.get()
    if not name:
        result_label.config(text="You must enter a word.", fg="red")
    else:
        counter = len(name)
        result_label.config(text=f"{name} has {counter} characters", fg="green")

root = tk.Tk()
root.geometry("400x200")
root.title("Character Counter")
root.configure(bg="#C4E1FF")

name_var = tk.StringVar()
name_var.trace("w", count_chars)

entry = tk.Entry(root, textvariable=name_var, font=("Arial", 24))
entry.pack(pady=20)

result_label = tk.Label(root, font=("Arial", 24))
result_label.pack()

root.mainloop()