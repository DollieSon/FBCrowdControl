import crowdFunctions as cf

class commadDet:
    baseCost:int
    extraCost:int
    effect:callable
    baseTime:int
    confict:set
    
    def __init__(self,baseC:int,eCost:int,eff:callable,bT:int,con:set = ()) -> None:
        self.baseCost = baseC
        self.extraCost = eCost
        self.effect = eff
        self.baseTime = bT
        self.confict = con 




class centralModule:

    controller = cf.CrowdController()
    commands = {
        "RandomLook":commadDet(2,1,controller.random_direction,5,("YardStare")),
        "YardStare":commadDet(5,2,controller.disable_MouseMove,3,("RandomLook")),
        "Shont":commadDet(3,1,controller.disable_LeftClick,3,("Berserk")),
        "Minent":commadDet(3,1,controller.disable_RightClick,3,("Miner69er")),
        "Berserk":commadDet(4,1,controller.hold_left_click,4,("Shont")),
        "Miner69er":commadDet(4,1,controller.hold_right_click,4,("Minent")),
        "Courage":commadDet(2,1,controller.hold_forward,8,),
        "Cowardice":commadDet(2,1,controller.hold_backward,8),
        "TodaLeft":commadDet(2,1,controller.hold_left,5),
        "TodaRight":commadDet(2,1,controller.hold_right,5),
        "aRRent":commadDet(3,1,controller.disable_reload,10),
        "BunnyHop":commadDet(3,1,controller.bunny_hop,8),
        "Grounded":commadDet(3,1,controller.disable_spacebar,8),
        "MapBoy":commadDet(4,1,controller.tab_spam,5)
    }


    def __init__(self) -> None:
        pass

    def read(self,player:str,command:str) -> None:
        
        command = command.split(" ")
        if(command.__len__() != 2):
            print("Command Length Error")
            return
        
