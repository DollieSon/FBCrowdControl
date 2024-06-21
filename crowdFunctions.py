import pynput
import time
import threading
class CrowdController():
    disabled = set()
    keyboard_C = pynput.keyboard.Controller
    mouse_C = pynput.mouse.Controller

    def KC_event_filter(self,msg,data):
        if data.vkCode in self.disabled:
            pynput.keyboard.Listener.suppress_event(pynput.keyboard.Listener)
    
    def MC_event_filter(self,msg,data):
        if msg in self.disabled:
            pynput.mouse.Listener.suppress_event(pynput.mouse.Listener)

    def __init__(self) -> None:
        self.keyboard_C = pynput.keyboard.Listener(win32_event_filter=self.KC_event_filter)
        self.mouse_C = pynput.mouse.Listener(win32_event_filter=self.MC_event_filter)
        self.keyboard_C.start()
        self.mouse_C.start()

    def __enable_key(self,key,secs):
        time.sleep(secs)
        self.disabled.remove(key)   

    def disable_key(self,key,secs):
        self.disabled.add(key)
        t1 = threading.Thread(target=self.__enable_key, args=(key,secs))
        t1.start()

    def disable_LeftClick(self,secs):
        self.disable_key(0x201,secs)

    def disable_RightClick(self,secs):
        self.disable_key(0x204,secs)

    def disable_MouseMove(self,secs):
        self.disable_key(0x200,secs)
