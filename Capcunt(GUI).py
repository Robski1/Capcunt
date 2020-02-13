from pynput import keyboard
from pynput.keyboard import Key, Controller
import random
import threading
from tkinter import *

k = Controller()
numbers={"i":"1","e":"3","a":"4","s":"5","t":"7","g":"9","o":"0"}
special={"a":"₳","b":"฿","c":"₵","d":"Đ","e":"Ɇ","f":"₣","g":"₲","h":"Ⱨ","i":"ł","j":"J","k":"₭","l":"Ⱡ","m":"₥","n":"₦","o":"Ø","p":"₱","q":"Q","r":"Ɽ","s":"₴","t":"₮","u":"Ʉ","v":"V","w":"₩","x":"Ӿ","y":"Ɏ","z":"Ⱬ"}

global boolcaps
global boolspecial
global boolnumbers
boolcaps = False
boolspecial = False
boolnumbers = False

def allFalse():
    global boolcaps
    global boolspecial
    global boolnumbers
    global lbl3
    global lbl4
    global lbl5
    boolcaps = False
    boolspecial = False
    boolnumbers = False
    lbl3.config(text="OFF",font=('ariel', 23))
    lbl4.config(text="OFF",font=('ariel', 23))
    lbl5.config(text="OFF",font=('ariel', 23))

def onCaps():
    global boolcaps
    global lbl3
    boolcaps = True
    lbl3.configure(text="ON",font=('ariel', 23))

def onSpecial():
    global boolspecial
    global lbl4
    boolspecial = True
    lbl4.config(text="ON",font=('ariel', 23))

def onNumbers():
    global boolnumbers
    global lbl5
    boolnumbers = True
    lbl5.config(text="ON",font=('ariel', 23))

def listen():
    with keyboard.Listener(
        on_press=on_press) as listener:
        listener.join()

def on_press(key):
    chance=random.randint(0,1)
    if boolcaps:
        try:
            key=str(key).strip("'")
            key1=ord(key)
            if key1>96 and key1<123:
                if chance==1:
                    k.press(Key.backspace)
                    k.release(Key.backspace)
                    with k.pressed(Key.shift):
                        k.press("%s"%key)
                        k.release("%s"%key)
        except:
            None
    
    if boolspecial:
        try:
            chance=random.randint(0,2)
            key=str(key).strip("'")
            key1=ord(key)
            if key1>96 and key1<123:
                if key in special:
                    if chance==2:
                        k.press(Key.backspace)
                        k.release(Key.backspace)
                        k.press("%s"%special[key])
                        k.release("%s"%special[key])
        except:
            None
    
    if boolnumbers:
        try:
            key=str(key).strip("'")
            key1=ord(key)
            if key1>96 and key1<123:
                if key in numbers:
                    if chance==1:
                        k.press(Key.backspace)
                        k.release(Key.backspace)
                        k.press("%s"%numbers[key])
                        k.release("%s"%numbers[key])
        except:
            None

#window config
window = Tk()
window.title("CAPCUNT")
window.geometry("400x162")
window.configure(bg="black")

#buttons
button1 = Button(window, text="CAPS", command=onCaps)
button1.config(font=('ariel', 15))
button1.grid(column=0,row=0,sticky=N+S+E+W)

button2 = Button(window, text="SPECIAL", command=onSpecial)
button2.config(font=('ariel', 15))
button2.grid(column=0,row=1,sticky=N+S+E+W)

button3 = Button(window, text="NUMBERS", command=onNumbers)
button3.config(font=('ariel', 15))
button3.grid(column=0,row=2,sticky=N+S+E+W)

button4 = Button(window, text="STOP", command=allFalse)
button4.config(font=('ariel', 15))
button4.grid(column=0,row=3,sticky=N+S+E+W)

#labels
lbl=Label(window,text="Caps: ",bg="black",fg="green")
lbl.config(font=('ariel', 23))
lbl.grid(column=1, row=0)

lbl1=Label(window,text="   Special: ",bg="black",fg="green")
lbl1.config(font=('ariel', 23))
lbl1.grid(column=1, row=1)

lbl2=Label(window,text="      Numbers: ",bg="black",fg="green")
lbl2.config(font=('ariel', 23))
lbl2.grid(column=1, row=2)

global lbl3
global lbl4
global lbl5
lbl3=Label(window,text="OFF",bg="black",fg="green")
lbl3.config(text="OFF",font=('ariel', 23))
lbl3.grid(column=2, row=0)
lbl4=Label(window,text="OFF",bg="black",fg="green")
lbl4.config(text="OFF",font=('ariel', 23))
lbl4.grid(column=2, row=1)
lbl5=Label(window,text="OFF",bg="black",fg="green")
lbl5.grid(column=2, row=2)
lbl5.config(text="OFF",font=('ariel', 23))

threading.Thread(target=listen).start()
window.mainloop()