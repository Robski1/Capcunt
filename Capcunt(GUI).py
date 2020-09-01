from pynput import keyboard
from pynput.keyboard import Key, Controller
import random, sys, threading, os
from tkinter import *
from tkinter import messagebox

k = Controller()
numbers={"i":"1","e":"3","a":"4","s":"5","t":"7","g":"9","o":"0"}
special={"a":"₳","b":"฿","c":"₵","d":"Đ","e":"Ɇ","f":"₣","g":"₲","h":"Ⱨ","i":"ł","j":"J","k":"₭","l":"Ⱡ","m":"₥","n":"₦","o":"Ø","p":"₱","q":"Q","r":"Ɽ","s":"₴","t":"₮","u":"Ʉ","v":"V","w":"₩","x":"Ӿ","y":"Ɏ","z":"Ⱬ"}
upsideDown={"a":"ɐ","b":"q","c":"ɔ","d":"p","e":"ǝ","f":"ⅎ","g":"ƃ","h":"ɥ","i":"ᴉ","j":"ɾ","k":"ʞ","l":"ʅ","m":"ɯ","n":"u","o":"o","p":"d","q":"b","r":"ɹ","s":"s","t":"ʇ","u":"n","v":"ʌ","w":"ʍ","x":"x","y":"ʎ","z":"z","1":"⇂","2":"↊","3":"↋","4":"ㄣ","5":"ϛ","6":"9","7":"𝘓","8":"8","9":"6","0":"0"}

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        os._exit(0)

global boolcaps
global boolspecial
global boolnumbers
global boolupsidedown
boolcaps = False
boolspecial = False
boolnumbers = False
boolupsidedown = False

def allFalse():
    global boolcaps
    global boolspecial
    global boolnumbers
    global boolupsidedown
    global lbl3
    global lbl4
    global lbl5
    global lbl7
    boolcaps = False
    boolspecial = False
    boolnumbers = False
    boolupsidedown = False
    
    lbl3.config(text="OFF",font=('ariel', 23))
    lbl4.config(text="OFF",font=('ariel', 23))
    lbl5.config(text="OFF",font=('ariel', 23))
    lbl7.config(text="OFF",font=('ariel', 23))

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

def onUpsideDown():
    global boolupsidedown
    global lbl7
    boolupsidedown = True
    lbl7.config(text="ON",font=('ariel', 23))

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
    
    if boolupsidedown:
        try:
            key=str(key).strip("'")
            key1=ord(key)
            if key1>96 and key1<123:
                if key in upsideDown:
                    if chance==1:
                        k.press(Key.backspace)
                        k.release(Key.backspace)
                        k.press("%s"%upsideDown[key])
                        k.release("%s"%upsideDown[key])
        except:
            None

#window config
window = Tk()
window.title("CAPCUNT")
window.geometry("500x205")
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

button4 = Button(window, text="UPSIDE DOWN", command=onUpsideDown)
button4.config(font=('ariel', 15))
button4.grid(column=0,row=3,sticky=N+S+E+W)

button5 = Button(window, text="STOP", command=allFalse)
button5.config(font=('ariel', 15))
button5.grid(column=0,row=4,sticky=N+S+E+W)

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

lbl6=Label(window,text="      Upside Down: ",bg="black",fg="green")
lbl6.config(font=('ariel', 23))
lbl6.grid(column=1, row=3)

global lbl3
global lbl4
global lbl5
global lbl7
lbl3=Label(window,text="OFF",bg="black",fg="green")
lbl3.config(text="OFF",font=('ariel', 23))
lbl3.grid(column=2, row=0)
lbl4=Label(window,text="OFF",bg="black",fg="green")
lbl4.config(text="OFF",font=('ariel', 23))
lbl4.grid(column=2, row=1)
lbl5=Label(window,text="OFF",bg="black",fg="green")
lbl5.grid(column=2, row=2)
lbl5.config(text="OFF",font=('ariel', 23))
lbl7=Label(window,text="OFF",bg="black",fg="green")
lbl7.grid(column=2, row=3)
lbl7.config(text="OFF",font=('ariel', 23))

window.protocol("WM_DELETE_WINDOW", on_closing)
thread = threading.Thread(target=listen).start()
window.mainloop()