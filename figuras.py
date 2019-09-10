from turtle import *
from tkinter import *

class circulo():
    def __init__(self,n):
        self.radio = n

    def obtenerD(self):
        return self.radio

    def area(self):
        return self.radio*self.radio*3.1415

class triangulo():
    def __init__(self,n):
        self.largo = n
        self.altura = 0

    def obtenerL(self):
        return self.largo

    def setAlt(self,n):
        self.altura=n

    def area(self):
        return self.radio*self.radio*3.1415

class rectangulo():
    def __init__(self,n):
        self.largo = n

    def obtenerL(self):
        return self.largo


def onCanvasClick(event):
    print
    'Got canvas click', event.x, event.y, event.widget


def onObjectClick(event):
    print
    'Got object click', event.x, event.y, event.widget,
    print
    event.widget.find_closest(event.x, event.y)


root = Tk()
canv = Canvas(root, width=100, height=100)
obj1 = canv.create_text(50, 30, text='Click me one')
obj2 = canv.create_text(50, 70, text='Click me two')

canv.bind('<Double-1>', onCanvasClick)
canv.tag_bind(obj1, '<Double-1>', onObjectClick)
canv.tag_bind(obj2, '<Double-1>', onObjectClick)
canv.pack()
root.mainloop()