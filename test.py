import pynput
import pynput.mouse as mouse
import time
from ctypes import wintypes
from pynput.mouse._win32 import Listener, WHEEL_DELTA
# Disable mouse and keyboard events

#supress leftclick using win32_event_filter
def test3():
    def win32_event_filter(msg,data):
        if(msg == 0x201):
            Listener.suppress_event(pynput.mouse.Listener)
    
    semething = mouse.Listener(win32_event_filter=win32_event_filter)
    semething.start()
    print("Mouse and keyboard events disabled")
    time.sleep(5)
    semething.stop()

#correct way to supress keyboard events
def test6():
    def win32_event_filter(msg, data):
        if data.vkCode == 0x58:
            Listener.suppress_event(pynput.keyboard.Listener)
    
    kl = pynput.keyboard.Listener(win32_event_filter=win32_event_filter)
    kl.start()
    print("Mouse and keyboard events disabled")
    time.sleep(5)
    kl.stop()

def test7():
    global disabled
    disabled = 0x60
    def win32_event_filter(msg, data):
        global disabled
        if data.vkCode == disabled:
            Listener.suppress_event(pynput.keyboard.Listener)
    

    kl = pynput.keyboard.Listener(win32_event_filter=win32_event_filter)
    kl.start()
    time.sleep(3)
    disabled = 0x58
    print("Mouse and keyboard events disabled")
    time.sleep(3)
    disabled = 0x59
    kl.stop()

test7()