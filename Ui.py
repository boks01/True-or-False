from tkinter import *
from tkinter import messagebox
BG = "#440A67"
CANVAS_BG = "#B4AEE8"   
class AppUi:
    def __init__(self):
        self.window = Tk()
        self.window.title("True or False?")
        self.window.config(padx=20, pady=20, bg=BG)
        self.canvas = Canvas(width=300, height=200, bg=CANVAS_BG, highlightthickness=0)
        self.text = self.canvas.create_text(
            150, 
            100, 
            width=290, 
            text="Quiz\nquestion", 
            font=("Roboto", 20, "bold"), 
            fill="white")
        self.canvas.grid(row=0, column=0, columnspan=2, pady=10)
        self.right_images = PhotoImage(file="images/true.png")
        self.wrong_images = PhotoImage(file="images/false.png")
        self.right_button = Button(image=self.right_images, highlightthickness=0)
        self.right_button.grid(row=1, column=0, pady=10)
        self.wrong_button = Button(image=self.wrong_images, highlightthickness=0)
        self.wrong_button.grid(row=1, column=1, pady=10)
        self.wm = Label(
            text="made by Salman.", 
            font=("Roboto", 10), 
            justify=CENTER, 
            bg=BG, 
            fg="white")
        self.wm.grid(row=2, column=0, columnspan=2)
        self.window.mainloop()