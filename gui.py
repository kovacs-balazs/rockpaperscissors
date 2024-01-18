from tkinter import PhotoImage
from game import start_game
import tkinter as tk


def open_gui():
    root.eval('tk::PlaceWindow . center')
    root.mainloop()


def rock_clicked():
    start_game("kő")


def paper_clicked():
    start_game("papír")


def scissors_clicked():
    start_game("olló")


root = tk.Tk()
root.title("RPS")
root.geometry("270x100")
root.resizable(False, False)

icon1 = PhotoImage(file="rock.png")
icon2 = PhotoImage(file="paper.png")
icon3 = PhotoImage(file="scissors.png")


button1 = tk.Button(root, image=icon1, compound=tk.LEFT, command=rock_clicked)
button2 = tk.Button(root, image=icon2, compound=tk.LEFT, command=paper_clicked)
button3 = tk.Button(root, image=icon3, compound=tk.LEFT, command=scissors_clicked)

button1.pack(side=tk.LEFT, padx=10)
button2.pack(side=tk.LEFT, padx=10)
button3.pack(side=tk.LEFT, padx=10)