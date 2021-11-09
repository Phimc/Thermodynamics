#"""分配初始位置(均匀)"""
import Constantnums as C
def ATOMS_INIT(ATOMS,n_gas):
    i = 0
    for x in range():
        for y in range():
            for z in range():
                ATOMS[i].r[0] = x*C.l/n_gas**(1/3)
                ATOMS[i].r[1] = y*C.l/n_gas**(1/3)
                ATOMS[i].r[2] = z*C.l/n_gas**(1/3)
                i += 1
    #"""分配初始速度"""
    v_mean = 1