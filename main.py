cartas = ["A","2","3","4","5","6","7","S","C","R"]
palos = ["o","c","b","e"]



def creaBaraja():
    baraja = []
    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)

    return baraja


baraja1 = creaBaraja() # meter la lista en una variable para poder imprimir varias 
baraja2 = creaBaraja()

print(baraja1)
'''
for palo in range (len(palos)):
    for carta in range ( len(cartas)):
        naipe = cartas[carta] + palos [palo]
        baraja.append(naipe)

si quiero crear la funcion con parameros podria ser crea_baraja(palos,cartas) y puedo crear las listas de la baraja francesa por ejemplo
'''

