import math as m
from random import*
import numpy as np
import matplotlib.pyplot as plt

n=30  #количесвтво частиц
dt=0.0001
E=5.6*10**3
D = 1000000*E
radius=5
time=1000
wallX1 = -250
wallX2 = 250
wallY1 = -250
wallY2 = 250
def force(r):
    return -24*E*(2*(radius/r)**12-(radius/r)**6)/r
def distance(el1, el2):
    return m.sqrt((particlesXcoordinate[el1] - particlesXcoordinate[el2])**2+(particlesYcoordinate[el1] - particlesYcoordinate[el2])**2)
def accelerationX(x):
    result = D*(radius/(wallX1-particlesXcoordinate[x]))**10 - D*(radius/(wallX2-particlesXcoordinate[x]))**10
    for el in range(n):
        if (el==x):
            result=result+0
        else:
            result = result + force(distance(el, x))*(particlesXcoordinate[x]-particlesXcoordinate[el])/distance(el, x) 
    return result/mass[x]
def accelerationY(x):
    result = D*(radius/(wallY1-particlesYcoordinate[x]))**10 - D*(radius/(wallY2-particlesYcoordinate[x]))**10
    for el in range(n):
        if (el==x):
            result=result+0
        else:
            result = result + force(distance(el, x))*(particlesYcoordinate[x]-particlesYcoordinate[el])/distance(el, x)
    return result/mass[x]
def kineticenergy():
    result = 0.
    for el in range(n):
        result = result + 0.5*mass[el]*particlesXvelocity[el]**2 + 0.5*mass[el]*particlesYvelocity[el]**2
    return result
def potentionalenergy():
    result = 0.
    for el in range(n):
        for ol in range(n):
            if(el==ol):
                result = result + 0
            else:
                result = result + 4*E*((radius/distance(el,ol)**12 - (radius/distance(el,ol)**6)))
    return result/2
particlesXcoordinate = [randint(-200., 200.) for i in range(n)]
particlesYcoordinate = [randint(-200., 200.) for i in range(n)]
particlesXvelocity = [randint(-50., 50.) for i in range(n)]
particlesYvelocity = [randint(-50., 50.) for i in range(n)]
mass = [0.5] * n
energyarray = [0] * time
for ul in range(time):
    for el in range(n):
        particlesXcoordinate[el] = particlesXcoordinate[el] + particlesXvelocity[el]*dt
        particlesYcoordinate[el] = particlesYcoordinate[el] + particlesYvelocity[el]*dt
    for el in range(n):
        particlesXvelocity[el] = particlesXvelocity[el] + accelerationX(el)*dt
        particlesYvelocity[el] = particlesYvelocity[el] + accelerationY(el)*dt
    energyarray[ul] = kineticenergy() + potentionalenergy()
x = np.arange(0, time+1, 1)
plt.plot(x, energyarray[x])
plt.show()