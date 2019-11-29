from pynput import keyboard
from pynput.keyboard import Key, Controller
import random
k = Controller()
numbers={"i":"1","e":"3","a":"4","s":"5","t":"7","g":"9","o":"0"}
special={"a":"₳","b":"฿","c":"₵","d":"Đ","e":"Ɇ","f":"₣","g":"₲","h":"Ⱨ","i":"ł","j":"J","k":"₭","l":"Ⱡ","m":"₥","n":"₦","o":"Ø","p":"₱","q":"Q","r":"Ɽ","s":"₴","t":"₮","u":"Ʉ","v":"V","w":"₩","x":"Ӿ","y":"Ɏ","z":"Ⱬ"}

def foo():
    global argument
    argument=input("Capcunt: ")
    while argument not in ["-n","numbers","--numbers","-c","caps","--caps","-s","special","--special","-h","help","--help"]:
        print("\nPlease type in a valid argument.")
        print("Type --help to see a list of possible commands (please note that you cant combine them at the moment)")
        argument=input("Capcunt: ")

    if argument=="-h" or argument=="--help" or argument=="help":
        print("\n\nHere is a list of the available comands:\n\n-h,help,--help\tDisplays a list of the available commands\n-c,caps,--caps\tSwitches out random characters for their capitalised counterpart\n-n,numbers,--numbers\tSwitches out some characters for numbers\n-s,special,--special\tSwitches out some characters for a special character\n")
        foo()
    else:
        listen()

def listen():
    print("Capcunt - RUNNING")
    with keyboard.Listener(
        on_press=on_press) as listener:
        listener.join()

def on_press(key):
    global argument
    chance=random.randint(0,1)
    if argument=="-c"or argument=="--caps" or argument=="caps":
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
    
    if argument=="-s" or argument=="--special" or argument=="special":
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
    
    if argument=="-n" or argument=="--numbers"or argument=="numbers":
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

print("Type --help to see a list of possible commands (please note that you cant combine them at the moment)")
foo()