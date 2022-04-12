# -*- coding: utf-8 -*-

import tkinter
from tkinter import *
import time
import tkinter as tk
import pygame

root = Tk()
root.geometry('600x600')
root.resizable(0,0)
root.config(bg ='gold1')
root.title('Running Timer')

canvas1 = tk.Canvas(root, width = 500, height = 400,bg='blanched almond')

canvas1.pack()

canvas1.place(x=50,y=70)
pygame.mixer.init()
Label(root, text = 'Running Timer' , font = 'arial 20 italic bold',  bg ='gold1').pack()
Label(root, font ='arial 15 bold', text = 'Current time :', bg = 'light green').place(x = 150 ,y = 170)


def clock():
    clock_time = time.strftime('%H:%M:%S %p')  #hours-00,minutes-00,seconds-00
    curr_time.config(text = clock_time)
    curr_time.after(1000,clock)
curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='blanched almond')
curr_time.place(x = 300 , y = 170)
clock()
sec = StringVar()
Entry(root, textvariable = sec, width = 2, font = 'arial 12').place(x=370, y=280)
sec.set("00")
mins= StringVar()
Entry(root, textvariable = mins, width =2, font = 'arial 12').place(x=345, y=280)
mins.set('00')
hrs= StringVar()
Entry(root, textvariable = hrs, width =2, font = 'arial 12').place(x=320, y=280)
hrs.set('00')

def countdown():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
     minute,second = (times // 60 , times % 60)
        
     hour = 0
     if minute > 60:
        hour , minute = (minute // 60 , minute % 60)
      
     sec.set(second)
     mins.set(minute)
     hrs.set(hour)
   
     root.update()
     time.sleep(1)
     
     if(times == 0):
            
         pygame.mixer.music.load("RunningAppAudio.mp3")
         pygame.mixer.music.play(loops=0)
         sec.set('00')
         mins.set('00')
         hrs.set('00')
      
     times -= 1
Label(root, font ='arial 15 bold', text = 'Set the time :',   bg ='light green').place(x = 170 ,y = 275)
Button(root, text='START', bd ='5', command = countdown, bg = 'gold2', font = 'arial 10 bold').place(x=260, y=370)

root.mainloop()
