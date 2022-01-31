from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from tkinter import *
from Tkinter.route import application


def change(window, option):
    window.destroy()
    application(option)


def start(window):
    window.title('Начало')
    window.resizable(False, False)
    label = Label(window, text="Выберете объект работы", font=('Arial', '12'))
    label.pack()
    button = Button(window, text="Работа с изображением", font=('Arial', '10'),
                    command =lambda:change(window,1))
    button.pack()
    button = Button(window, text="Работа с построенной деталью", font=('Arial', '10'),
                    command =lambda:change(window,2))
    button.pack()

    window.geometry('400x200')  # Размер окна

def first_screen():
    window = Tk()
    start(window)
    window.mainloop()


if __name__ == '__main__':
    first_screen()


