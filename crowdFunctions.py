import pynput
import time
import threading
import ctypes
import pyautogui
import random
import win32api, win32con
u32 = ctypes.windll.user32
ScreenSize = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
print(ScreenSize)

class CrowdController():
    disabled = set()
    # isInverted = False
    keyboard_C = pynput.keyboard.Controller
    mouse_C = pynput.mouse.Controller
    mouse_L = pynput.mouse.Listener
    def KC_event_filter(self,msg,data):
        if data.vkCode in self.disabled:
            pynput.keyboard.Listener.suppress_event(pynput.keyboard.Listener)
    
    def MC_event_filter(self,msg,data):
        if msg in self.disabled:
            pynput.mouse.Listener.suppress_event(pynput.mouse.Listener)
        # if self.isInverted and msg == 0x200:
        #     data.pt.x = ScreenSize[0] - data.pt.x
        #     data.pt.y = ScreenSize[1] - data.pt.y
        #     self.mouse_C.position = (data.pt.x, data.pt.y)
        #     pynput.mouse.Listener.suppress_event(pynput.mouse.Listener)


    def __init__(self) -> None:
        self.keyboard_L = pynput.keyboard.Listener(win32_event_filter=self.KC_event_filter)
        self.mouse_L = pynput.mouse.Listener(win32_event_filter=self.MC_event_filter)
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

    
    # def __enableInvert(self,secs:int,mt):
    #     time.sleep(secs)
    #     self.isInverted = False

    # def invertMouse(self,dur):
    #     self.isInverted = True
    #     t1 = threading.Thread(target=self.__enableInvert, args=(dur,3))
    #     t1.start()
    def __moveRandom(self,directions):
        for dir in directions:
            sleep = random.randint(1,2)
            distance = random.randint(100,500)
            xmult = 0
            ymult = 0
            if dir == 1:
                xmult = 0
                ymult = 1
            elif dir == 2:
                xmult = 0
                ymult = -1
            elif dir == 3:
                xmult = 1
                ymult = 0
            elif dir == 4:
                xmult = -1
                ymult = 0
            elif dir == 5:
                xmult = 1
                ymult = 1
            elif dir == 6:
                xmult = -1
                ymult = 1
            elif dir == 7:
                xmult = -1
                ymult = -1
            elif dir == 8:
                xmult = 1
                ymult = -1
            x = self.mouse_C.position[0] + distance*xmult
            y = self.mouse_C.position[1] + distance*ymult
            print("Moving to: ",x,y)
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y, 0, 0)
            self.mouse_C.position = (x,y)
            time.sleep(sleep)

    def random_direction(self,num_dir):
        directions = [random.randint(1,8) for _ in range(num_dir)]
        print(directions)
        t1 = threading.Thread(target=self.__moveRandom, args=([directions]))
        t1.start()