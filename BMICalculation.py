import tkinter as tk

from tkinter import *


root= tk.Tk()
root.title("BMI calculator")
root.geometry("600x600")
root .configure(background="lavender")
BMI=StringVar()

def bmi():

    

   h=float(entry1.get())

   w=float(entry2.get())

   bmi =float (w/(h*h))

   BMI.set(bmi)

   
L = tk.Label(root,text='BMI RANGE     -     HEALTH STATUS\n    18.5    -    Unerweight\n18.5—24.9    -    Healthy\n25.0—29.9     -     Overweight\n30.0 and Above  	-     Obese',bg='light yellow',fg='black')
L.configure(font=("Helvetica 11 bold"))
L.pack(side='bottom')
L1 =tk. Label(root, text="Calculate your BMI",bg="midnight blue",fg='white')
L1.pack(side='top')
L1.place(x=250,y=20)
canvas1 = tk.Canvas(root, width = 400, height = 300,bg='dodgerblue4')
canvas1.pack()
canvas1.place(x=100,y=70)
entry1 = tk.Entry (root)
canvas1.create_window(250, 100, window=entry1)
entry2 = tk.Entry (root)
canvas1.create_window(250, 140, window=entry2)
entry3 = tk.Entry (root,textvariable=BMI)
canvas1.create_window(250, 180, window=entry3)
label1 = tk.Label(root, text="Enter your height(in m)",bg='dodgerblue4',fg='white')
canvas1.create_window(100, 100, window=label1)
label2 = tk.Label(root, text="Enter your weight(in kg)",bg='dodgerblue4',fg='white')
canvas1.create_window(100, 140, window=label2)
label3 = tk.Label(root, text="Your BMI is :",bg='dodgerblue4',fg='white')
canvas1.create_window(100, 180, window=label3)
btn = Button(root, text = "Calculate", bg='midnight blue',fg='white',command=bmi)
btn.pack(side = 'top')
btn.place(x=270,y=300)

root.mainloop()
