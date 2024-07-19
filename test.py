import pynput
import pynput.mouse as mouse
import time
from ctypes import wintypes
from pynput.mouse._win32 import Listener, WHEEL_DELTA
import threading
import crowdFunctions as cf
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

def test4():
    global disabled
    disabled = set()
    def enable_key(key,secs):
        global disabled
        time.sleep(secs)
        disabled.remove(key)
    def disable_left_click(secs):
        global disabled
        disabled.add(0x201)
        t1 = threading.Thread(target=enable_key, args=(0x201,secs))
        t1.start()

    def win32_event_filter(msg,data):
        if msg in disabled:
            Listener.suppress_event(pynput.mouse.Listener)
    
    semething = mouse.Listener(win32_event_filter=win32_event_filter)
    semething.start()
    print("Mouse and keyboard events disabled")
    disable_left_click(5)
    print("This should still run")
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

#random move test
def test8():
    CrowdController = cf.CrowdController()
    time.sleep(5)
    # CrowdController.disable_LeftClick(5)
    CrowdController.random_direction(5)
    #disable Mouse
    #CrowdController.disable_MouseMove(5)
    
def test9():
    CrowdController = cf.CrowdController()
    time.sleep(5)
    CrowdController.invertMouse(5)

def test10():
    CrowdController = cf.CrowdController()
    time.sleep(5)
    print("disabling w")
    CrowdController.hold_left(5)

def test11():
    CrowdController = cf.CrowdController()
    CrowdController.read("Ray Anthony","Shont 5")
test11()
