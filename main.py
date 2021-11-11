import atom
import ATOMS_init
import Statistic as Stat
import Constantnums as C
n_gas = 1000
#"""生成粒子"""
ATOMS = [atom.atom() for i in range(n_gas)] #"""气体分子数"""
ATOMS_init.ATOMS_INIT(ATOMS,n_gas)
t=0
while True:
    print(ATOMS[102].r)
    print(ATOMS[0].rv)
    Stat.atom_r(ATOMS)
    #p = Stat.V_distribution(ATOMS)
    #Stat.draw(p)
    for atom in ATOMS:
        atom.fresh()
    t += C.dt
    if t // 1E-6:
        Stat.atom_r(ATOMS)
        print(t)
        if t == 5E-6:
            break