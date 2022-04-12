# -*- coding: utf-8 -*-


from tkinter import *
import tkinter as tk
import pygame
import time

root= tk.Tk()
root.title("Water tracking")
root.geometry("600x600")
root .configure(background="Dodgerblue4")
Water=StringVar()
pygame.mixer.init()

def close():
   root.destroy()
   

def show():
   
   root.deiconify()
   
   button.config(text = 'Close', command = close)
   
   root.after(5000, hide)

    

def hide():
   
   root.withdraw()
   time_to_sleep = set_time_to_sleep.get()
   time_to_sleep = float(time_to_sleep)
   #print time_to_sleep
   time.sleep(time_to_sleep)
   
   pygame.mixer.music.load(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\iraznay.mp3")
   pygame.mixer.music.play(loops=0)
   show()
   

def water():

    
   p=int(entry0.get())
   h=int(entry1.get())

   w=int(entry2.get())

   water =int(w+(h*60)+(p*3600))

   Water.set(water)

   


canvas1 = tk.Canvas(root, width = 400, height = 300,bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=100,y=70)
entry0 = tk.Entry (root)
canvas1.create_window(250, 60, window=entry0)
entry1 = tk.Entry (root)
canvas1.create_window(250, 100, window=entry1)
entry2 = tk.Entry (root)
canvas1.create_window(250, 140, window=entry2)
set_time_to_sleep = tk.Entry (root,textvariable=Water)
canvas1.create_window(1000, 1000, window=set_time_to_sleep)
button = Button(text = 'Set Time',command=hide)
button.pack()
button.place(x=270,y=340)
L=tk.Label(root,text="Water tracker",bg='midnight blue',fg='white')
L.pack()
L.place(x=250,y=10)
label1 = tk.Label(root, text="Enter hour of interval :",bg='dodgerblue4',fg='white')
canvas1.create_window(100, 60, window=label1)
label2 = tk.Label(root, text="Enter minutes of interval :",bg='dodgerblue4',fg='white')
canvas1.create_window(100, 100, window=label2)
label3 = tk.Label(root, text="Enter seconds of interval :",bg='dodgerblue4',fg='white')
canvas1.create_window(100, 140, window=label3)
label4=tk.Label(root,text="Hydrate yourself , drink a glass of water!!",bg='midnight blue',fg='white')
label4.pack()
label4.place(x=170,y=400)
btn = Button(root, text = "Calculate Interval in total seconds ", bg='midnight blue',fg='white',command=water)
btn.pack(side = 'top')
btn.place(x=200,y=270)

root.mainloop()
