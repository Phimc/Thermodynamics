import math
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
            self.rv[i] += self.ra[i]*C.dt
    
    def force(self,atom):
        r = math.sqrt((self.r[0]-atom.r[0])**2+(self.r[1]-atom.r[1])**2+(self.r[2]-atom.r[2])**2)
        F = 12*C.epsilon/C.sigma((C.sigma/r)**13-(C.sigma/r)**7)
        a = [
        self.r[0]-atom.r[0]/r/self.m,
        self.r[1]-atom.r[1]/r/self.m,
        self.r[2]-atom.r[2]/r/self.m] 
"""
def collipsion(ATOMS):
    for atomi in ATOMS:
        for atomj in ATOMS:
            if atom_
            """