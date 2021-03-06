import math as m
from random import*
import yaml

n=90  #количесвтво частиц
dt=0.0001
E=5.6*10**3
D = 1000000*E
radius=10
time=10000
wallX1 = -150*radius
wallX2 = 150*radius
wallY1 = -150*radius
wallY2 = 150*radius
massa = 0.5

def force(r):
    f=(radius**2/r)**3
    return -24*E*f*(f-1)/m.sqrt(r)

def distancesquare(el1, el2):
    return (particlesXcoordinate[el1] - particlesXcoordinate[el2])**2+(particlesYcoordinate[el1] - particlesYcoordinate[el2])**2

def accelerationX(x):
    result = D*(radius/(wallX1-particlesXcoordinate[x]))**10 - D*(radius/(wallX2-particlesXcoordinate[x]))**10
    for el in range(n):
        if (el==x):
            result=result+0
        else:
            d = distancesquare(el,x)
            result = result + force(d)*(particlesXcoordinate[x]-particlesXcoordinate[el])/m.sqrt(d) 
    return result/mass[x]

def accelerationY(x):
    result = D*(radius/(wallY1-particlesYcoordinate[x]))**10 - D*(radius/(wallY2-particlesYcoordinate[x]))**10
    for el in range(n):
        if (el==x):
            result=result+0
        else:
            d = distancesquare(el,x)
            result = result + force(d)*(particlesYcoordinate[x]-particlesYcoordinate[el])/m.sqrt(d)
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
                f = (radius**2/distancesquare(el,ol))**3
                result = result + 4*E*f*(f - 1)
    result = result/2

    for el in range(n):
        r1 = (radius/(particlesXcoordinate[el] - wallX1))**2
        r2 = (radius/(particlesXcoordinate[el] - wallX2))**2 
        r3 = (radius/(particlesYcoordinate[el] - wallY1))**2 
        r4 = (radius/(particlesYcoordinate[el] - wallY2))**2
        result = result + D*(r1**4.5 + r2**4.5 + r3**4.5 + r4**4.5) 
    return result
    
particlesXcoordinate = [randint(-500., 500.) for i in range(n)]
particlesYcoordinate = [randint(-500., 500.) for i in range(n)]
particlesXvelocity = [randint(-50., 50.) for i in range(n)]
particlesYvelocity = [randint(-50., 50.) for i in range(n)]
particlesXacceleration1 = [0]*n
particlesYacceleration1 = [0]*n
particlesXacceleration2 = [0]*n
particlesYacceleration2 = [0]*n
mass = [massa] * n
with open('данные/example.yml', 'r') as f:
    loaded = yaml.safe_load(f)
loaded['usefulparameters'].append({'number': n,'time': time, 'E':E, 'D': D, 'radius': radius, 'wallX1': wallX1, 'wallX2': wallX2,
                                    'wallY1': wallY1, 'wallY2': wallY2, 'massa': massa})
loaded['usefulparameters'].pop(0)
for el in range(n):
    particlesXacceleration1[el] = accelerationX(el)
    particlesYacceleration1[el] = accelerationY(el)

for ul in range(time):
    for el  in range(n):
        particlesXcoordinate[el] = particlesXcoordinate[el] + particlesXvelocity[el]*dt + 0.5*particlesXacceleration1[el]*dt**2
        particlesYcoordinate[el] = particlesYcoordinate[el] + particlesYvelocity[el]*dt + 0.5*particlesYacceleration1[el]*dt**2
    for el in range(n):
        particlesXacceleration2[el] = accelerationX(el)
        particlesYacceleration2[el] = accelerationY(el)
    for el in range(n):
        particlesXvelocity[el] = particlesXvelocity[el] + 0.5*(particlesXacceleration1[el] + particlesXacceleration2[el])*dt
        particlesYvelocity[el] = particlesYvelocity[el] + 0.5*(particlesYacceleration1[el] + particlesYacceleration2[el])*dt
    for el in range(n):
        particlesXacceleration1[el] = particlesXacceleration2[el]
        particlesYacceleration1[el] = particlesYacceleration2[el]
    for el in range(n):
        loaded['results'].append({'number':ul*n+el,'xcoordinates':particlesXcoordinate[el],'ycoordinates':particlesYcoordinate[el],
                                   'xvelocitys':particlesXvelocity[el],'yvelositys':particlesYvelocity[el]})

loaded['results'].pop(0)
with open('данные/parameters.yml', 'w') as f:
    yaml.dump(loaded, f)