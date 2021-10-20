import numpy as np
import matplotlib.pyplot as plt
import yaml
import math as m
with open ('данные/parameters.yml', "r") as f:
    loaded = yaml.safe_load(f)
n = loaded['usefulparameters'][0].get('number')
E = loaded['usefulparameters'][0].get('E')
D = loaded['usefulparameters'][0].get('D')
time = loaded['usefulparameters'][0].get('time')
radius = loaded['usefulparameters'][0].get('radius')
massa = loaded['usefulparameters'][0].get('massa')
wallX1 = loaded['usefulparameters'][0].get('wallX1')
wallX2 = loaded['usefulparameters'][0].get('wallX2')
wallY1 = loaded['usefulparameters'][0].get('wallY1')
wallY2 = loaded['usefulparameters'][0].get('wallY2')
res = loaded['results']

def distancesquare(el1, el2):
    return (xcoordinate[el1] - xcoordinate[el2])**2+(ycoordinate[el1] - ycoordinate[el2])**2

def kineticenergy():
    result = 0.
    for el in range(n):
        result = result + 0.5*massa*xvelocity[el]**2 + 0.5*massa*yvelocity[el]**2
    return result

def potentionalenergy():
    result = 0.
    for el in range(n):
        for ol in range(el+1, n):
            f = (radius**2/distancesquare(el,ol))**3
            result = result + 4*E*f*(f - 1)

    for el in range(n):
        r1 = m.abs(radius/(xcoordinate[el] - wallX1))
        r2 = m.abs(radius/(xcoordinate[el] - wallX2)) 
        r3 = m.abs(radius/(ycoordinate[el] - wallY1))
        r4 = m.abs(radius/(ycoordinate[el] - wallY2))
        result = result + D*(r1**9 + r2**9 + r3**9 + r4**9) 
    return result

xcoordinate = [0]*n
ycoordinate = [0]*n
xvelocity = [0]*n
yvelocity = [0]*n
kinenergy = [0]*time
totalenergy = [0]*time
x = np.arange(0, time, 1)

for ul in range(time):
    countparticles = res[ul*n:(ul+1)*n]
    print(countparticles)
    for el in range(n):
        xcoordinate[el] = countparticles[el].get('xcoordinate').copy()
        print(type(xcoordinate[el]))
        ycoordinate[el] = countparticles[el].get('ycoordinate')
        xvelocity[el] = countparticles[el].get('xvelocity')
        yvelocity[el] = countparticles[el].get('yvelocity')
    print(type(xcoordinate[1]))
    kinenergy[ul] = kineticenergy()
    totalenergy[ul] = potentionalenergy() + kinenergy[ul]
kinenergy  = np.array(kinenergy)
totalenergy = np.array(totalenergy)
plt.figure()
plt.plot(x, kinenergy[x])

plt.figure()
plt.plot(x, totalenergy[x])

plt.show()


