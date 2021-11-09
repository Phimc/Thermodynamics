import atom
import ATOMS_init
n_gas = 1000
#"""生成粒子"""
ATOMS = [atom.atom() for i in range(n_gas)] #"""气体分子数"""
ATOMS_init.ATOMS_INIT(ATOMS,n_gas)

while True:
    print(ATOMS[10].r)
    print(ATOMS[0].rv)
    break