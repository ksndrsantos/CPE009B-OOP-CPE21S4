from tkinter import *

class MyWindow:
    def __init__(self, win):
        win.configure(bg="#FFDFD6")
        # common widget
        self.Label1 = Label(win, fg="Brown", bg="pink", text="-- The Best Calculator --", font=("Century Gothic Bold", 20))
        self.Label1.place(x=100, y=20)
        self.Label2 = Label(win, fg="Green", bg="pink", text="Number 1: ", font=("Century Gothic Bold", 10))
        self.Label2.place(x=125, y=80)
        self.Entry1 = Entry(win, bd=6)
        self.Entry1.place(x=225, y=80)
        self.Label3 = Label(win, fg="Green", bg="pink", text="Number 2: ", font=("Century Gothic Bold", 10))
        self.Label3.place(x=125, y=125)
        self.Entry2 = Entry(win, bd=6)
        self.Entry2.place(x=225, y=125)
        self.Label4 = Label(win, fg="Brown", bg="pink", text="Result: ",font=("Century Gothic Bold", 10))
        self.Label4.place(x=125, y=175)
        self.Entry3 = Entry(win, bd=6)
        self.Entry3.place(x=225, y=175)
        self.Button1 = Button(win, fg="Brown", text="add",font=("Century Gothic Bold", 10), command=self.add)
        self.Button1.place(x=75, y=275)
        self.Button2 = Button(win, fg="Brown", text="sub", font=("Century Gothic Bold", 10), command=self.subtract)
        self.Button2.place(x=175, y=275)
        self.Button3 = Button(win, fg="Brown", text="mul", font=("Century Gothic Bold", 10),command=self.multiply)
        self.Button3.place(x=275, y=275)
        self.Button4 = Button(win, fg="Brown", text="div", font=("Century Gothic Bold", 10),command=self.divide)
        self.Button4.place(x=375, y=275)
        self.Label1 = Label(win, fg="Brown", bg="pink", text=" : ̗̀➛Choose your operator", font=("Century Gothic Bold", 15))
        self.Label1.place(x=120, y=225)


    def add(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 + num2
        self.Entry3.delete(0, 'end')
        self.Entry3.insert(END, str(result))

    def subtract(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1 - num2
        self.Entry3.delete(0, 'end')
        self.Entry3.insert(END, str(result))

    def multiply(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1*num2
        self.Entry3.delete(0, 'end')
        self.Entry3.insert(END, str(result))

    def divide(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        result = num1/num2
        self.Entry3.delete(0, 'end')
        self.Entry3.insert(END, str(result))

window = Tk()
MyWin = MyWindow(window)

window.geometry("500x500+10+10")
window.title("Standard Calculator")
window.mainloop()
