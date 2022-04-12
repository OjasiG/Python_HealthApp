# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image 

root=Tk()
root.geometry("1000x600")
root.configure(background="dodgerblue4")
root.title("Sleep Recommendations")
L=tk.Label(root,text='Recommended Sleep Durations According to Age',font=("Arial bold ",18),bg='dodger blue4',fg='white')
L.pack()
L1=tk.Label(root,text='\nPrioritizing good sleep is a sign of self love!',font=("Arial Italic",17),bg='dodger blue4',fg='white')
L1.pack()
image1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\PSDL mini-project\sleep.png")
test = ImageTk.PhotoImage(image1)
resize_image = image1.resize((680,450))
new_image= ImageTk.PhotoImage(resize_image)

label1 = tk.Label(image=new_image)
label1.image = new_image
label1.pack()
label1.place(x=150,y=100)



root.mainloop()