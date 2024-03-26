import tkinter as tk
from random import randint
from tkinter import messagebox

def on_submit():
    value = int(field.get())
    abs(target - value)
    if previous_difference is None or difference < previous_difference:
        messagebox.showinfo(('Stan','Robi się cieplej'))
    else:
        messagebox.showinfo(('Stan','Robi się zimniej'))

    previous_difference = difference

previous_difference = None
target = randint(1, 100)
#tworzenie okienka
window = tk.Tk()
window.title('Zgadnij liczbę')
#tworzenie label wraz z informacją że bedzie zarejestrowane w window, mozna przekazac text, kolor,styl tego pola itd
label = tk.Label(window, text='Wprowadź liczbę')
#umieszczanie label w oknie
label.pack()
#wprowadzenie pola na liczbę:
field = tk.Entry()
field.pack()
#button dodajemy poprzez: dodajemy text i command czyli to co ma sie wydarzyc kiedy ten tekst zostanie przekazany -> tworzymy funkcje
#w ramach funkcji on_submit mozemy pobrac sobie wartosc z naszego pola czyli value=field.get()
button = tk.Button(text='Zgaduje!', command=on_submit)
button.pack()

window.mainloop()
