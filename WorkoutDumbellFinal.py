# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import messagebox

root=Tk()
root.geometry("1000x600")
root.configure(background="dodgerblue4")
root.title("Workout charts-with dumbells")

L=tk.Label(root,text='Try these workouts and get abs you dreamt of!!',font=("Arial bold ",18),bg='dodger blue4',fg='white')
L.pack()


image1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\workouts1D.jpg")
test = ImageTk.PhotoImage(image1)
resize_image = image1.resize((300,220))
new_image= ImageTk.PhotoImage(resize_image)


image2 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\workouts2D.jpg")
test2 = ImageTk.PhotoImage(image2)
resize_image2 = image2.resize((300,220))
new_image2= ImageTk.PhotoImage(resize_image2)

image3 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\workouts3D.jpg")
test3 = ImageTk.PhotoImage(image3)
resize_image3 = image3.resize((300,220))
new_image3 = ImageTk.PhotoImage(resize_image3)

image4 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\workouts4D.jpg")
test4 = ImageTk.PhotoImage(image4)
resize_image4 = image4.resize((300,220))
new_image4 = ImageTk.PhotoImage(resize_image4)

image5 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\workouts5D.jpg")
test5 = ImageTk.PhotoImage(image5)
resize_image5 = image5.resize((300,220))
new_image5 = ImageTk.PhotoImage(resize_image5)

image6 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\workouts6D.jpg")
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

# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
 
# setting the default value as 0
hour.set("00")
minute.set("02")
second.set("00")
 
# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=110,y=285)
 
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=160,y=285)
 
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=210,y=285)
 
 
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
 
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
 
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
 
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1
 
# button widget
btn = Button(root, text='Start', bd='5',
             command= submit)
btn.place(x = 55,y = 80)
hour1=StringVar()
minute1=StringVar()
second1=StringVar()
 
# setting the default value as 0
hour1.set("00")
minute1.set("01")
second1.set("00")
 
# Use of Entry class to take input from the user
hourEntry1= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour1)
hourEntry1.place(x=420,y=285)
 
minuteEntry1= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute1)
minuteEntry1.place(x=470,y=285)
 
secondEntry1= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second1)
secondEntry1.place(x=520,y=285)
 
 
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp1 = int(hour1.get())*3600 + int(minute1.get())*60 + int(second1.get())
    except:
        print("Please input the right value")
    while temp1 >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins1,secs1 = divmod(temp1,60)
 
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours1=0
        if mins1 >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours1, mins1 = divmod(mins1, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour1.set("{0:2d}".format(hours1))
        minute1.set("{0:2d}".format(mins1))
        second1.set("{0:2d}".format(secs1))
 
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
 
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp1 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp1 -= 1
 
# button widget
btn1 = Button(root, text='Start', bd='5',
             command= submit)
btn1.place(x = 360,y = 80)
hour2=StringVar()
minute2=StringVar()
second2=StringVar()
 
# setting the default value as 0
hour2.set("00")
minute2.set("03")
second2.set("30")
 
# Use of Entry class to take input from the user
hourEntry2= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour2)
hourEntry2.place(x=730,y=285)
 
minuteEntry2= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute2)
minuteEntry2.place(x=780,y=285)
 
secondEntry2= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second2)
secondEntry2.place(x=830,y=285)
 
 
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp2 = int(hour2.get())*3600 + int(minute2.get())*60 + int(second2.get())
    except:
        print("Please input the right value")
    while temp2 >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins2,secs2 = divmod(temp2,60)
 
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours2=0
        if mins2 >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours2, mins2 = divmod(mins2, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour2.set("{0:2d}".format(hours2))
        minute2.set("{0:2d}".format(mins2))
        second2.set("{0:2d}".format(secs2))
 
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
 
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp2 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp2 -= 1
 
# button widget
btn2 = Button(root, text='Start', bd='5',
             command= submit)
btn2.place(x = 670,y = 80)

hour3=StringVar()
minute3=StringVar()
second3=StringVar()
 
# setting the default value as 0
hour3.set("00")
minute3.set("01")
second3.set("30")
 
# Use of Entry class to take input from the user
hourEntry3= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour3)
hourEntry3.place(x=110,y=550)
 
minuteEntry3= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute3)
minuteEntry3.place(x=160,y=550)
 
secondEntry3= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second3)
secondEntry3.place(x=210,y=550)
 
 
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp3 = int(hour3.get())*3600 + int(minute3.get())*60 + int(second3.get())
    except:
        print("Please input the right value")
    while temp3 >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins3,secs3 = divmod(temp3,60)
 
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours3=0
        if mins3 >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours3, mins3 = divmod(mins3, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour3.set("{0:2d}".format(hours3))
        minute3.set("{0:2d}".format(mins3))
        second3.set("{0:2d}".format(secs3))
 
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
 
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp3 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp3 -= 1
 
# button widget
btn3 = Button(root, text='Start', bd='5',
             command= submit)
btn3.place(x = 55,y = 330)

hour5=StringVar()
minute5=StringVar()
second5=StringVar()
 
# setting the default value as 0
hour5.set("00")
minute5.set("02")
second5.set("00")
 
# Use of Entry class to take input from the user
hourEntry5= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour5)
hourEntry5.place(x=420,y=550)
 
minuteEntry5= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute5)
minuteEntry5.place(x=470,y=550)
 
secondEntry5= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second5)
secondEntry5.place(x=520,y=550)
 
 
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp5 = int(hour5.get())*3600 + int(minute5.get())*60 + int(second5.get())
    except:
        print("Please input the right value")
    while temp5 >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins5,secs5 = divmod(temp5,60)
 
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours5=0
        if mins5 >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours5, mins5 = divmod(mins5, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour5.set("{0:2d}".format(hours5))
        minute5.set("{0:2d}".format(mins5))
        second5.set("{0:2d}".format(secs5))
 
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
 
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp5 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp5 -= 1
 
# button widget
btn5 = Button(root, text='Start', bd='5',
             command= submit)
btn5.place(x = 360,y = 330)
hour6=StringVar()
minute6=StringVar()
second6=StringVar()
 
# setting the default value as 0
hour6.set("00")
minute6.set("00")
second6.set("30")
 
# Use of Entry class to take input from the user
hourEntry6= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour6)
hourEntry6.place(x=730,y=550)
 
minuteEntry6= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute6)
minuteEntry6.place(x=780,y=550)
 
secondEntry6= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second6)
secondEntry6.place(x=830,y=550)
 
 
def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp6 = int(hour6.get())*3600 + int(minute6.get())*60 + int(second6.get())
    except:
        print("Please input the right value")
    while temp6 >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins6,secs6 = divmod(temp6,60)
 
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours6=0
        if mins6 >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours6, mins6 = divmod(mins6, 60)
         
        # using format () method to store the value up to
        # two decimal places
        hour6.set("{0:2d}".format(hours6))
        minute6.set("{0:2d}".format(mins6))
        second6.set("{0:2d}".format(secs6))
 
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)
 
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp6 == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp6 -= 1
 
# button widget
btn6 = Button(root, text='Start', bd='5',
             command= submit)
btn6.place(x = 670,y = 330)

root.mainloop()
