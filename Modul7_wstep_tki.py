import tkinter as tk

def send_name():
    print(first_name.get())
    print('click')

window = tk.Tk()
window.title('Pystart')

label = tk.Label(window, text="Jak masz na imię?")
label.pack()

first_name = tk.Entry()
first_name.pack()

button = tk.Button(text="OK", command=send_name)
button.pack()

window.mainloop()