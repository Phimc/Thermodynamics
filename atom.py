import Constantnums as C
class atom():
    def __init__(self):
        self.m = C.m
        self.r = [0,0,0]
        self.rv = [0,0,0]
        self.ra = [0,0,0]

    def fresh(self):
        for i in range(3):
            self.r[i] += self.rv[i]*C.dt
    
