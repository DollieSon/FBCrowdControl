import pynput
import time
import threading
class CrowdController():
    disabled = set()
    isInverted = False
    keyboard_C = pynput.keyboard.Controller
    mouse_C = pynput.mouse.Controller
    mouse_L = pynput.mouse.Listener
    def KC_event_filter(self,msg,data):
        if data.vkCode in self.disabled:
            pynput.keyboard.Listener.suppress_event(pynput.keyboard.Listener)
    
    def MC_event_filter(self,msg,data):
        if msg in self.disabled:
            pynput.mouse.Listener.suppress_event(pynput.mouse.Listener)

    def invertedMove(self,x,y):
        if self.isInverted:
            self.mouse_C.position = (x,y)

    def __init__(self) -> None:
        self.keyboard_L = pynput.keyboard.Listener(win32_event_filter=self.KC_event_filter)
        self.mouse_L = pynput.mouse.Listener(win32_event_filter=self.MC_event_filter, on_move=self.invertedMove)
        self.mouse_C = pynput.mouse.Controller()
        self.keyboard_L.start()
        self.mouse_L.start()

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

    
    def __enableInvert(self,secs:int,mt):
        time.sleep(secs)
        self.isInverted = False

    def invertMouse(self,dur):
        self.isInverted = True
        t1 = threading.Thread(target=self.__enableInvert, args=(dur,3))
        t1.start()
