from tkinter import *
from RingBuffer import *


pb = PriorityRingBuffer(10)

def add():
    var = entry.get().split(",")
    var[0] = int(var[0])
    pb.add(Pair(var[0] , var[1]))

def showBuffer():
    if str(pb) == "":
        show.set("Стек пустой")
    else:
        show.set(str(pb))

def minimum():
    show.set(str(pb.extract_minimum()))
    

root = Tk()
root.title("Search Tree")
root.geometry("300x300")
show = StringVar()
entry = StringVar()



addButton = Button(root, text="добавить элемент" , command = add)
addButton.place(x=0, y=0, width=150, height=50)

addEntry = Entry(root , textvariable = entry)
addEntry.place(x=150, y=0, width=150, height=50)
showButton = Button(root, text="показать стек" , command = showBuffer)
showButton.place(x=0, y=50, width=150, height=50)

showButton = Button(root, text="показать элемент с\nминимальным\nприоритетом"  , command = lambda : minimum())
showButton.place(x=150, y=50, width=150, height=50)

showLabel = Label(root, textvariable=show)
showLabel.place(x=0, y=100, width=300, height=200)

root.mainloop()
