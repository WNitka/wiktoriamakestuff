import math


# trojkat

a = 10
b = 20
c = 15
h = 12

obwod = a + b + c
pole = int((h * a) / 2)

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynisi " + str(pole) + ".")

#romb

a1=20
h1=10

pole_romb = 4*a1
obwod_romb = a1*h1

print("Obwod rombu wynosi " + str(obwod_romb) + ", zas pole wynisi " + str(pole_romb) + ".")

#kolo

pi = math.pi
r=10

pole_kolo = pi*r**2
obwod_kolo = pi*r*2

print("Obwod kola wynosi " + str(obwod_kolo) + ", zas pole wynisi " + str(pole_kolo) + ".")


