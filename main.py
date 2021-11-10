import atom
import ATOMS_init
import Statistic as Stat
n_gas = 1000
#"""生成粒子"""
ATOMS = [atom.atom() for i in range(n_gas)] #"""气体分子数"""
ATOMS_init.ATOMS_INIT(ATOMS,n_gas)

while True:
    print(ATOMS[102].r)
    print(ATOMS[0].rv)
    #p = Stat.V_distribution(ATOMS)
    #Stat.draw(p)
    break