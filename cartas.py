import random

cartas = ("A","2","3","4","5","6","7","S","C","R")
palos = ("o","c","b","e")

def creaBaraja():
    baraja = []
    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)

    return baraja

def mezclar (b):
    br = []
    i = 0
    while i < 40:
        n = random.randint(0,39)
        while b [n] in br:
            n = random.randint(0,39)
        br.append(b[n])
        i+=1
    b=br

    return b

def repartir ( b, players, cards):
    #res = [[]]* players no puede ser porque te coge tres veces la misma lista
    
    res= []
    for p in range (players):
        res.append([])

    for ij in range (players):
        for ic in range (cards):
            carta = b.pop(0)
            res[ic].append(carta)

    return res





'''
for palo in range (len(palos)):
    for carta in range ( len(cartas)):
        naipe = cartas[carta] + palos [palo]
        baraja.append(naipe)

si quiero crear la funcion con parameros podria ser crea_baraja(palos,cartas) y puedo crear las listas de la baraja francesa por ejemplo
'''

