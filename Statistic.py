import math
import matplotlib.pyplot as plt
def v(atom):
    v = math.sqrt(atom.rv[0]**2+atom.rv[1]**2+atom.rv[2]**2)
    return v
def V_distribution(ATOMS):
    v_diction={}
    for atom in ATOMS:
        k = v(atom)//10
        if k in v_diction:
            v_diction[k]+=1
        else:
            v_diction[k]=1
    return v_diction

"""
def draw(diction):
    x = []
    y = []
    for i in diction.keys():
        x.append(i)
        y.append(diction[i])
    plt.scatter(x,y)
    plt.show()
    return 0
"""