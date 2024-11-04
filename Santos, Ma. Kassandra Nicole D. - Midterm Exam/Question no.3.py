from tkinter import *

class MyWindow:
    def __init__(self, win):
        win.configure(bg="white")
        self.Label2 = Label(win, fg="Black", bg="white", text="Enter your Fullname: ", font=("Century Gothic Bold", 10))
        self.Label2.place(x=50, y=83)
        self.Entry1 = Entry(win, bd=6)
        self.Entry1.place(x=225, y=80)
        self.Button1 = Button(win, fg="Black", text="Click to Display your Fullname", font=("Century Gothic Bold", 10), command=self.display)
        self.Button1.place(x=20, y=150)
        self.Label3 = Label(win, fg="Black", bg="white", font=("Century Gothic Bold", 10))
        self.Label3.place(x=250, y=150)

    def display(self):
        fullname = self.Entry1.get()
        self.Label3.config(text=f"{fullname}")


window = Tk()
MyWin = MyWindow(window)

window.geometry("500x500+10+10")
window.title("Midterm In OOP")
window.mainloop()
