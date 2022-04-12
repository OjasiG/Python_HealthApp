# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
import pygame
import time
from tkinter import messagebox
from tkcalendar import Calendar
import datetime

root= tk.Tk()
root.geometry("600x600")
root.configure(background="coral3")
root.title("Period Tracker")
today = datetime.date.today()
Water=StringVar()



def close():
   root.destroy()
   

def show():
   messagebox.askokcancel("Period Tracker", "Red days Here...")
   
   root.deiconify()
 
   
   button.config(text = 'Stop my period tracking', command = close)
   
   root.after(3000, hide)
   

def hide():
   
   root.withdraw()
   time_to_sleep = set_time_to_sleep.get()
   time_to_sleep = float(time_to_sleep)
   #print time_to_sleep
   time.sleep(time_to_sleep)

   show()

def water():

   water = 5

   Water.set(water)


Label(root, text = 'Period Tracker' , font = 'arial 20 italic bold',  bg ='coral3').pack()
canvas1 = tk.Canvas(root, width = 500, height = 400,bg='blanched almond')
canvas1.pack()
canvas1.place(x=50,y=70)
set_time_to_sleep = tk.Entry(root,textvariable=Water)
canvas1.create_window(1000, 1000, window=set_time_to_sleep)
button = Button(text = 'Set my tracking from today!',command=hide)
button.pack()
button.place(x=220,y=440)
btn = Button(root, text = "Click this when your red days start", bg='coral3',fg='black',command=water)
btn.pack(side = 'top')
btn.place(x=200,y=400)
cal = Calendar(root,year=today.year, month=today.month, day=today.day )
cal.pack(padx=30 ,pady = 50)

 
def grad_date():
    date.config(text = "Today's Date is: " + cal.get_date())
 
# Add Button and Label
btn1=Button(root, text = "Get Date", command = grad_date)
btn1.pack(pady = 1)
btn1.place(x=265,y=300)

def log():
    now = datetime.datetime.now()
    start_time = now.strftime("%H:%M:%S")
    with open("log.txt", 'a') as f:
        f.write(f"Your period came today: {now}\n")
    return 0

btn2 = Button(root, text = "Note Date",command = log)
btn2.pack(pady = 2)
btn2.place(x=260,y=360)
date = Label(root, text = "")
date.pack(pady = 2)

root.mainloop()
