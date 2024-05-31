
import tkinter as tk
from tkinter import *
import pygame

win = tk.Tk()
win.title("IBM")
win.geometry("600x500+10+20")

pygame.mixer.init()
def play():
    pygame.mixer.music.load("C:\Training\PycharmProjects\IBMBatch03\Day10\music.wav")
    pygame.mixer.music.play(loops=0)

lbl= Label(win, text="MUSIC PLAYER", bd=9, relief=GROOVE, font=("Arial", 22))
lbl.pack(side=TOP)

btn = Button(win, text="Play", font=("Hellvetica", 32), command=play)
btn.pack(pady=20)

win.mainloop()