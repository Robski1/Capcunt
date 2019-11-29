from pynput import keyboard
from pynput.keyboard import Key, Controller
import random
k = Controller()

def on_press(key):
    chance=random.randint(0,1)
    try:
        key=str(key).strip("'")

        key1 = ord(key)
        if key1 > 96 and key1 < 123:
            if chance==1:
                k.press(Key.backspace)
                k.release(Key.backspace)
                with k.pressed(Key.shift):
                    k.press("%s"%key)
                    k.release("%s"%key)
    except:
        None

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
