class Mobile:

    def __init__(self, name, price):
        pass

    def calling(self):
        print("Mobile called")

    def sms(self):
        print("Mobile sms called")

    def game(self):
        print("Mobile game called")

class REALME_XT(Mobile):
    def __init__(self, name, price):
        pass

    def cam(self):
        print("Mobile cam")

    def music(self):
        print("Mobile music")

    def vedio_call(self):
        print("Mobile vedio_call called")

REALME_XT=REALME_XT("REALME_XT",100)
REALME_XT.sms()
REALME_XT.game()
REALME_XT.music()
REALME_XT.vedio_call()

