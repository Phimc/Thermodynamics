#"""分配初始位置(均匀)"""
from numpy import random as rd
import Constantnums as C
import math 
v_mean = (8*C.R*C.T/C.Pi/C.M)**(1/2)
def randangle():
    angle = [math.cos(rd.rand()*C.Pi),math.cos(rd.rand()*C.Pi),math.cos(rd.rand()*C.Pi)]
    return angle
def ATOMS_INIT(ATOMS,n_gas):
    i = 0
    for x in range(10):
        for y in range(10):
            for z in range(10):
                ATOMS[i].r[0] = x*C.l/n_gas**(1/3)
                ATOMS[i].r[1] = y*C.l/n_gas**(1/3)
                ATOMS[i].r[2] = z*C.l/n_gas**(1/3)
                
                v = randspeed()
                v_angle = randangle()
                ATOMS[i].rv[0] = v_angle[0]*v
                ATOMS[i].rv[1] = v_angle[1]*v
                ATOMS[i].rv[2] = v_angle[2]*v

                i += 1
                if i > n_gas:
                    return 0
#"""分配初始速度"""
def randspeed():
    v = v_mean*rd.rand()*2
    return v