# -*- coding: utf-8 -*-


import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time 
from tkinter import messagebox


root=Tk()
root.geometry("1000x600")
root.configure(background="dodgerblue4")
root.title("Workout charts-without dumbells")

L=tk.Label(root,text='No dumbells?No worries!\nTry these workouts and get abs you dreamt of!!',font=("Arial bold ",18),bg='dodger blue4',fg='white')
L.pack()

image1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\w1N.png")
test = ImageTk.PhotoImage(image1)
resize_image = image1.resize((300,220))
new_image= ImageTk.PhotoImage(resize_image)


image2 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\w2N.png")
test2 = ImageTk.PhotoImage(image2)
resize_image2 = image2.resize((300,220))
new_image2= ImageTk.PhotoImage(resize_image2)

image3 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\w3N.png")
test3 = ImageTk.PhotoImage(image3)
resize_image3 = image3.resize((300,220))
new_image3 = ImageTk.PhotoImage(resize_image3)

image4 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\w4N.png")
test4 = ImageTk.PhotoImage(image4)
resize_image4 = image4.resize((300,220))
new_image4 = ImageTk.PhotoImage(resize_image4)

image5 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\w5N.png")
test5 = ImageTk.PhotoImage(image5)
resize_image5 = image5.resize((300,220))
new_image5 = ImageTk.PhotoImage(resize_image5)

image6 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\w6N.png")
test6 = ImageTk.PhotoImage(image6)
resize_image6 = image6.resize((300,220))
new_image6 = ImageTk.PhotoImage(resize_image6)


label1 = tk.Label(image=new_image)
label1.image = new_image
label1.pack()
label1.place(x=40,y=60)


label2 = tk.Label(image=new_image2)
label2.image = new_image2
label2.pack()
label2.place(x=40,y=320)


label3 = tk.Label(image=new_image3)
label3.image = new_image3
label3.pack()
label3.place(x=350,y=320)


label4 = tk.Label(image=new_image4)
label4.image = new_image4
label4.pack()
label4.place(x=350,y=60)

label5 = tk.Label(image=new_image5)
label5.image = new_image5
label5.pack()
label5.place(x=660,y=60)

label6 = tk.Label(image=new_image6)
label6.image = new_image6
label6.pack()
label6.place(x=660,y=320)

hour1=StringVar()
minute1=StringVar()
second1=StringVar()
 
hour1.set("00")
minute1.set("01")
second1.set("00")
 
hour1Entry= Entry(root, width=3, font=("Arial",18,""), textvariable=hour1)
hour1Entry.place(x=110,y=285)
 
minute1Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=minute1)
minute1Entry.place(x=160,y=285)
 
second1Entry= Entry(root, width=3, font=("Arial",18,""), textvariable=second1)
second1Entry.place(x=210,y=285)
 
 
def submit():
    try:
        temp1 = int(hour1.get())*3600 + int(minute1.get())*60 + int(second1.get())
    except:
        print("Please input the right value")
    while temp1 >-1:
         
        mins1,secs1 = divmod(temp1,60)
 
        hours1=0
        if mins1 >60:
             
            hours1, mins1 = divmod(mins1, 60)
         
        hour1.set("{0:2d}".format(hours1))
        minute1.set("{0:2d}".format(mins1))
        second1.set("{0:2d}".format(secs1))
 
        root.update()
        time.sleep(1)
        
        if (temp1 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
        temp1 -= 1
 
btn1 = Button(root, text='Start', bd='5',command= submit)
btn1.place(x = 65,y = 80)


hour2=StringVar()
minute2=StringVar()
second2=StringVar()
 
hour2.set("00")
minute2.set("01")
second2.set("30")
 
hour2Entry= Entry(root, width=3, font=("Arial",18,""), textvariable=hour2)
hour2Entry.place(x=420,y=285)
 
minute2Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=minute2)
minute2Entry.place(x=470,y=285)
 
second2Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=second2)
second2Entry.place(x=520,y=285)
 
 
def submit():
    try:
        temp2 = int(hour2.get())*3600 + int(minute2.get())*60 + int(second2.get())
    except:
        print("Please input the right value")
    while temp2 >-1:
         
        mins2,secs2 = divmod(temp2,60)
 
        hours2=0
        if mins2 >60:
             
            hours2, mins2 = divmod(mins2, 60)
         
        hour2.set("{0:2d}".format(hours2))
        minute2.set("{0:2d}".format(mins2))
        second2.set("{0:2d}".format(secs2))
 
        root.update()
        time.sleep(1)
        
        if (temp2 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
        temp2 -= 1
 
btn2 = Button(root, text='Start', bd='5',command= submit)
btn2.place(x = 375,y = 80)


hour3=StringVar()
minute3=StringVar()
second3=StringVar()
 
hour3.set("00")
minute3.set("01")
second3.set("00")
 
hour3Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=hour3)
hour3Entry.place(x=730,y=285)
 
minute3Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=minute3)
minute3Entry.place(x=780,y=285)
 
secondEntry= Entry(root, width=3, font=("Arial",18,""),textvariable=second3)
secondEntry.place(x=830,y=285)
 
 
def submit():
    try:
        temp3 = int(hour3.get())*3600 + int(minute3.get())*60 + int(second3.get())
    except:
        print("Please input the right value")
    while temp3 >-1:
         
        mins3,secs3 = divmod(temp3,60)
 
        hours3=0
        if mins3 >60:
             
            hours3, mins3 = divmod(mins3, 60)
         
        hour3.set("{0:2d}".format(hours3))
        minute3.set("{0:2d}".format(mins3))
        second3.set("{0:2d}".format(secs3))
 
        root.update()
        time.sleep(1)
 
        if (temp3 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        temp3 -= 1
 
btn3 = Button(root, text='Start', bd='5',command= submit)
btn3.place(x = 670,y = 70)


hour4=StringVar()
minute4=StringVar()
second4=StringVar()
 
hour4.set("00")
minute4.set("01")
second4.set("00")
 
hour4Entry= Entry(root, width=3, font=("Arial",18,""), textvariable=hour4)
hour4Entry.place(x=110,y=555)
 
minute4Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=minute4)
minute4Entry.place(x=160,y=555)
 
second4Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=second4)
second4Entry.place(x=210,y=555)
 
 
def submit():
    try:
        temp4 = int(hour4.get())*3600 + int(minute4.get())*60 + int(second4.get())
    except:
        print("Please input the right value")
    while temp4 >-1:
         
        mins4,secs4 = divmod(temp4,60)
 
        hours4=0
        if mins4 >60:
             
            hours4, mins4 = divmod(mins4, 60)
         
        hour4.set("{0:2d}".format(hours4))
        minute4.set("{0:2d}".format(mins4))
        second4.set("{0:2d}".format(secs4))
 
        root.update()
        time.sleep(1)
 
        if (temp4 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        temp4 -= 1
 
btn4 = Button(root, text='Start', bd='5',command= submit)
btn4.place(x = 65,y = 330)

hour5=StringVar()
minute5=StringVar()
second5=StringVar()
 
hour5.set("00")
minute5.set("02")
second5.set("00")
 
hour5Entry= Entry(root, width=3, font=("Arial",18,""), textvariable=hour5)
hour5Entry.place(x=420,y=555)
 
minute5Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=minute5)
minute5Entry.place(x=470,y=555)
 
second5Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=second5)
second5Entry.place(x=520,y=555)
 
 
def submit():
    try:
        temp5 = int(hour5.get())*3600 + int(minute5.get())*60 + int(second5.get())
    except:
        print("Please input the right value")
    while temp5 >-1:
         
        mins5,secs5 = divmod(temp5,60)
 
        hours5=0
        if mins5 >60:
             
            hours5, mins5 = divmod(mins5, 60)
         
        hour5.set("{0:2d}".format(hours5))
        minute5.set("{0:2d}".format(mins5))
        second5.set("{0:2d}".format(secs5))
 
        root.update()
        time.sleep(1)
 
        if (temp5 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        temp5 -= 1
 
btn5 = Button(root, text='Start', bd='5',command= submit)
btn5.place(x = 365,y = 330)

hour6=StringVar()
minute6=StringVar()
second6=StringVar()
 
hour6.set("00")
minute6.set("00")
second6.set("45")
 
hour6Entry= Entry(root, width=3, font=("Arial",18,""), textvariable=hour6)
hour6Entry.place(x=730,y=555)
 
minute6Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=minute6)
minute6Entry.place(x=780,y=555)
 
second6Entry= Entry(root, width=3, font=("Arial",18,""),textvariable=second6)
second6Entry.place(x=830,y=555)
 
 
def submit():
    try:
        temp6 = int(hour6.get())*3600 + int(minute6.get())*60 + int(second6.get())
    except:
        print("Please input the right value")
    while temp6 >-1:
         
        mins6,secs6 = divmod(temp6,60)
 
        hours6=0
        if mins6 >60:
             
            hours6, mins6 = divmod(mins6, 60)
         
        hour6.set("{0:2d}".format(hours6))
        minute6.set("{0:2d}".format(mins6))
        second6.set("{0:2d}".format(secs6))
 
        root.update()
        time.sleep(1)
 
        if (temp6 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        temp6 -= 1
 
btn6 = Button(root, text='Start', bd='5',command= submit)
btn6.place(x = 670,y = 330)

root.mainloop()