import math
import Constantnums as C
v_distribute = {}
def maxwell():
    global v_distribute
    dv = 1 #dv=1m/s
    P_others = 0
    for i in range(20000):
        P_vi = 4*C.Pi*(C.M/(2*C.Pi*C.R*C.T))**(3/2)*math.exp(-C.M*(dv*i)**2/(2*C.R*C.T))*(dv*i)**2*dv
        P_others += P_vi
        v_distribute[P_vi]=i*dv
    return 0
maxwell()