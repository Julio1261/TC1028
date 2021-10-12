'''
Julio Bayliss
A00227244
11/10/2021
TC1028 G3
'''

# ACTIVIDAD 23

# GitHub

fo = open('control.txt', 'r')
turno = fo.readline()
fo.close()

print(turno)

if (turno == '1'):
    print('Yey! Es mi turno')


# abre batalla y adiciona algo JUGADOR 1
    fo = open("batalla.txt", "a")
    fo.write("Jugador1")
    fo.close()

# prepara el archivo CONTROL para que siga el turno J2
    fo = open("control.txt", "w")
    fo.write("2")
    fo.close()

# avisa que paso
    print("\n\n\nHola todo mundo ")
    print("Ya realice mi batalla y modifiqué el archivo batalla.txt")
    print("También modifiqué el archivo control.txt para permitir al J2 su turno.")
    print("Esperaré un rato a ver si le intento de nuevo ...")
else:
    print("No es mi turno,,, bye")