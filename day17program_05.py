from tkinter import *
master=Tk()
demo_text="this a sample demo of message widget."
msg=Message(master,text=demo_text)
msg.config(bg='pink',font=('times',24,'bold'))
msg.pack()
