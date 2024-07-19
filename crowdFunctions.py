import pynput
import time
import threading
import ctypes
import pyautogui
import random
import win32api, win32con
import mysql.connector
import datetime
u32 = ctypes.windll.user32
ScreenSize = u32.GetSystemMetrics(0), u32.GetSystemMetrics(1)
print(ScreenSize)

class commadDet:
    baseCost:int
    extraCost:int
    effect:callable
    baseTime:int
    
    def __init__(self,baseC:int,eCost:int,eff:callable,bT:int) -> None:
        self.baseCost = baseC
        self.extraCost = eCost
        self.effect = eff
        self.baseTime = bT



class CrowdController():
    disabled = set()
    keyboard_C = pynput.keyboard.Controller
    mouse_C = pynput.mouse.Controller
    mouse_L = pynput.mouse.Listener

    BASEPLAYERPOINTS = 10
    MINUTESPERPOINT = 3

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fbplays"
    )
    """
    """

    def KC_event_filter(self,msg,data):
        if data.vkCode in self.disabled:
          pynput.keyboard.Listener.suppress_event(pynput.keyboard.Listener)
        if data.vkCode in self.disabled and msg == 0x0101: # ox101 is the up event
            pynput.keyboard.Listener.suppress_event(pynput.keyboard.Listener)
    
    def MC_event_filter(self,msg,data):
        if msg in self.disabled:
            pynput.mouse.Listener.suppress_event(pynput.mouse.Listener)


    def __init__(self) -> None:
        self.keyboard_L = pynput.keyboard.Listener(win32_event_filter=self.KC_event_filter)
        self.mouse_L = pynput.mouse.Listener(win32_event_filter=self.MC_event_filter)
        self.mouse_C = pynput.mouse.Controller()
        self.keyboard_C = pynput.keyboard.Controller()
        self.keyboard_L.start()
        self.mouse_L.start()

    def __enable_key(self,key,secs):
        time.sleep(secs)
        self.disabled.remove(key)   

    def _disable_key(self,key,secs):
        if key in self.disabled:
            return -1
        self.disabled.add(key)
        t1 = threading.Thread(target=self.__enable_key, args=(key,secs))
        t1.start()

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

    def __holdKbd(self,key,secs):
        if key in self.disabled:
            return -1
        self.disabled.add(key)
        secs *=10
        while secs > 0:
            win32api.keybd_event(key, 0, 0, 0)
            time.sleep(0.1)
            secs -= 1
        self.disabled.remove(key)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

    def __spamKey(self,key,secs,delay=0.1,wait=0):
        if key in self.disabled:
            return -1
        self.disabled.add(key)
        secs *=int(1/(delay+wait))
        while secs > 0:
            win32api.keybd_event(key, 0, 0, 0)
            time.sleep(delay)
            win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(wait)
            secs -= 1
        self.disabled.remove(key)
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)


    # Proper Functions

    def disable_LeftClick(self,secs):
        self._disable_key(0x201,secs)

    def disable_RightClick(self,secs):
        self._disable_key(0x204,secs)

    def disable_MouseMove(self,secs):
        self._disable_key(0x200,secs)

    def disable_reload(self,secs):
        self._disable_key(0x52,secs)

    def disable_spacebar(self,secs):
        self._disable_key(0x20,secs)

    def hold_left_click(self,secs):
        self.mouse_C.press(pynput.mouse.Button.left)
        self._disable_key(0x202,secs)

    def hold_right_click(self,secs):
        self.mouse_C.press(pynput.mouse.Button.right)
        self._disable_key(0x205,secs)
    
    def hold_forward(self,secs):
        t1 = threading.Thread(target=self.__holdKbd, args=(0x57,secs))
        t1.start()

    def hold_backward(self,secs):
        t1 = threading.Thread(target=self.__holdKbd, args=(0x53,secs))
        t1.start()

    def hold_left(self,secs):
        t1 = threading.Thread(target=self.__holdKbd, args=(0x41,secs))
        t1.start()

    def hold_right(self,secs):
        t1 = threading.Thread(target=self.__holdKbd, args=(0x44,secs))
        t1.start()

    def bunny_hop(self,secs):
        t1 = threading.Thread(target=self.__spamKey, args=(0x20,secs))
        t1.start()

    def tab_spam(self,secs):
        t1 = threading.Thread(target=self.__spamKey, args=(0x09,secs,0.2,0.5))
        t1.start()

    def random_direction(self,num_dir):
        directions = [random.randint(1,8) for _ in range(num_dir)]
        print(directions)
        t1 = threading.Thread(target=self.__moveRandom, args=([directions]))
        t1.start()


    commands = {
        "RandomLook":commadDet(2,1,random_direction,5),
        "YardStare":commadDet(5,2,disable_MouseMove,3),
        "Shont":commadDet(3,1,disable_LeftClick,3),
        "Minent":commadDet(3,1,disable_RightClick,3),
        "Berserk":commadDet(4,1,hold_left_click,4),
        "Miner69er":commadDet(4,1,hold_right_click,4),
        "Courage":commadDet(2,1,hold_forward,8,),
        "Cowardice":commadDet(2,1,hold_backward,8),
        "TodaLeft":commadDet(2,1,hold_left,5),
        "TodaRight":commadDet(2,1,hold_right,5),
        "aRRent":commadDet(3,1,disable_reload,10),
        "BunnyHop":commadDet(3,1,bunny_hop,8),
        "Grounded":commadDet(3,1,disable_spacebar,8),
        "MapBoy":commadDet(4,1,tab_spam,5)
    }

    """
    return values
    0 = Success
    1 = Command Length Error
    2 = Command Not Found
    3 = Command Conflict
    4 = Points not Enough   
    """
    def read(self,player:str,command:str) -> int: #command = "command secs"
        # update player table
        #check if player in db
        cursor = self.database.cursor()
        print(type(player))
        cursor.execute("SELECT * FROM maintable WHERE name = '"+player+"'")
        result = cursor.fetchall()
        if(result.__len__() == 0):
            cursor.execute("INSERT INTO maintable (name,points,last_update) VALUES (%s,%s,%s)",(player,self.BASEPLAYERPOINTS,datetime.datetime.now()))
            self.database.commit()
        command = command.split(" ")
        if(command.__len__() != 2):
            print("Command Length Error")
            return 1
        if(command[0] not in self.commands.keys()):
            print("Command Not Found")
            return 2
        command[1] = int(command[1])
        # print("Secs: ",command[1])
        if(command[1] <= self.commands[command[0]].baseTime):
            command[1] = self.commands[command[0]].baseTime
        cost = (command[1] - self.commands[command[0]].baseTime) * self.commands[command[0]].extraCost + self.commands[command[0]].baseCost
        print("Time:",command[1])
        print("Cost: ",cost)
        # reduce player points
        cursor.execute("SELECT points FROM maintable WHERE name = '"+player+"'")
        result = cursor.fetchall()
        playerPoints = result[0][0]
        if( playerPoints< cost):
            print("Points not Enough")
            return 4
        playerPoints -= cost
        isgood = self.commands[command[0]].effect(self,command[1])
        if(isgood == -1):
            print("Command Conflict")
            return 3
        cursor.execute("UPDATE maintable SET points = %s WHERE name = %s",(playerPoints,player))
        # update last_update
        cursor.execute("UPDATE maintable SET last_update = %s WHERE name = %s",(datetime.datetime.now(),player))
        #execute command
        self.database.commit()
        return 0
