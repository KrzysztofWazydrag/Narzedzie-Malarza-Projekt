#1. Napisz program, który pyta użytkownika o jego imie i nazwisko
# oraz zapisuje te informacje w pliku tekstowym
#2. Stwórz interfejs graficzny do powyższego programu
# Jeśli imię i nazwisko występowało już wcześniej w pliku
# to wyświetl komunikat informujący o tym i nie dodawaj duplikatu.

import tkinter as tk
from tkinter import messagebox

def add_person():
    persons = set()
    with open('full_name.txt') as file:
        for line in file:
            first_name, last_name = line.strip().split(' ')
            persons.add(
                (first_name, last_name)
            )


    with open('full_name.txt', 'a', encoding='utf8') as file:
        if (first_name_entry.get(), last_name_entry.get()) not in persons:
            file.write(f'{first_name_entry.get()} {last_name_entry.get()}\n')
        else:
            messagebox.showinfo(title='Uważaj!', message = 'Ta osoba już była na liście')

window = tk.Tk()
window.title('Dodaj osobę')

first_name_label = tk.Label(window, text='Podaj imie: ')
first_name_label.pack()
first_name_entry = tk.Entry()
first_name_entry.pack()

last_name_label = tk.Label(window, text='Podaj nazwisko: ')
last_name_label.pack()
last_name_entry = tk.Entry()
last_name_entry.pack()

button = tk.Button(text='Dodaj', command=add_person)
button.pack()

window.mainloop()


# first_name = input('Podaj imie: ')
# last_name = input('Podaj nazwisko: ')
#
# with open('full_name.txt', 'a', encoding='utf8') as file:
#     file.write(f'{first_name} {last_name}\n')