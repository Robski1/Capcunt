from pynput import keyboard
from pynput.keyboard import Key, Controller
import random
import threading
from tkinter import *
import time

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
    boolcaps = False
    boolspecial = False
    boolnumbers = False
    print("all false")

def onCaps():
    global boolcaps
    boolcaps = True
    print("boolcaps: ",boolcaps)

def onSpecial():
    global boolspecial
    boolspecial = True
    print("special: ",boolspecial)

def onNumbers():
    global boolnumbers
    boolnumbers = True
    print("numbers: ",boolnumbers)

def listen():
    with keyboard.Listener(
        on_press=on_press) as listener:
        print("listener joined")
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

#tkinter 
window = Tk()
window.title("CAPCUNT")
window.geometry("300x150")

button1 = Button(window, text="CAPS", command=onCaps)
button1.config(font=('ariel', 15))
button1.grid(column=1,row=0)

button2 = Button(window, text="SPECIAL", command=onSpecial)
button2.config(font=('ariel', 15))
button2.grid(column=1,row=1)

button3 = Button(window, text="NUMBERS", command=onNumbers)
button3.config(font=('ariel', 15))
button3.grid(column=2,row=0)

button4 = Button(window, text="STOP", command=allFalse)
button4.config(font=('ariel', 15))
button4.grid(column=2,row=1)

threading.Thread(target=listen).start()
window.mainloop()