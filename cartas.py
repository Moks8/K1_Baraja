cartas = ["A","2","3","4","5","6","7","S","C","R"]
palos = ["o","c","b","e"]



def creaBaraja():
    baraja = []
    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)

    return baraja
