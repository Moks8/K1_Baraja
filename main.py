cartas = ["A","2","3","4","5","6","7","S","C","R"]
palos = ["o","c","b","e"]

baraja = []

for palo in palos:
    for carta in cartas:
        naipe = cartas + palos
        baraja.append(naipe)
'''
for palo in range (len(palos)):
    for carta in range ( len(cartas)):
        naipe = cartas[carta] + palos [palo]
        baraja.append(naipe)

'''

print(baraja)