import random


def Gano_el_jugador(jugador, oponente):
    # retorna el valor true (verdadero) si el jugador
    # piedra gana a tigera (pi>ti)
    # tigeta le gana a piedra (ti>pi)
    # papel le gana a piedra(pa>pi)
    if ((jugador == 'pi' and oponente == 'ti')
            or (jugador == 'ti' and oponente == 'pa')
            or (jugador == 'pa' and oponente == 'pi')):

        return True
    else:
        return False


def jugar():
    usuario = input("escoge una opcion:'pi'para pierda 'pa'para papel 'ti'para tigera \n").lower()
    print("Tu seleccion:",usuario)
    computadora = random.choice(['pi', 'ti', 'pa'])
    print("Selección de la computadora:", computadora)
    if usuario == computadora:
        return 'Empate!'
    if Gano_el_jugador(usuario, computadora):
        return 'ganaste'
    return 'perdiste'


print(jugar())