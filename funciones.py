def tradletra(letra):
    if letra == "a":
        return 0
    elif letra == "b":
        return 1   
    elif letra == "c":
        return 2 
    elif letra == "d":
        return 3 
    elif letra == "e":
        return 4 
    elif letra == "f":
        return 5
    elif letra == "g":
        return 6
    elif letra == "h":
        return 7
    elif letra == "i":
        return 8
    elif letra == "j":
        return 9

def cualp(cuad, most, p):
    datos = open('data.txt', 'r') 
    temp1 = datos.readline()
    temp2 = datos.readline()
    temp3 = datos.readline()
    if p==1:
        temp3 = datos.readline()
    datos.close()
    datos = open('data.txt', 'w')
    if p==1:
        datos.write(cuad)
        datos.write(temp2)
        datos.write(most)
        datos.write(temp3)
    else:
        datos.write(temp1)
        datos.write(cuad)
        datos.write(temp3)
        datos.write(most)
    datos.close()

def verRespuestas(p):
    datos = open('data.txt', 'r')
    linea=datos.readline()
    if p==2:
        linea=datos.readline()
    for j in range(10):
        for i in range(20):
            print(linea[i+j*20], end='')
        print()

    datos.close()

def ver(p):
    datos = open('data.txt', 'r')
    linea=datos.readline()
    linea=datos.readline()
    linea=datos.readline()
    if p==2:
        linea=datos.readline()
    for j in range(10):
        for i in range(20):
            print(linea[i+j*20], end='')
        print()

    datos.close()

def readMaxPoints(p, np):
    points = open('puntaje.txt', 'r')
    temp1 = points.readline()
    temp2 = points.readline()
    if p==2:
        temp3 = points.readline()
        puntosm = points.readline()
    else:
        puntosm = points.readline()
        temp3 = points.readline()
    points.close()

    puntosm=str(int(puntosm)+np)

    points = open('puntaje.txt', 'w')
    points.write(temp1)
    points.write(temp2)
    if p==2:
        points.write(temp3)
        points.write(puntosm)
    else:
        points.write(puntosm)
        points.write('\n')
        points.write(temp3)
    points.close()

    if int(temp3)==int(puntosm):
        print('El Juego está listo para jugarse.')
    else:
        print('El juego no está balanceado.')

def checkwin(p,new):
    if p==1:
        p=2
    else:
        p=1

    puntaje = open('puntaje.txt', 'r')
    current1 = puntaje.readline()
    current2 = puntaje.readline()
    if p==1:
        current1=int(current1)+new
    else:
        current2=int(current2)+new
    
    max1 = puntaje.readline()
    max2 = puntaje.readline()

    puntaje.close()

    puntaje = open('puntaje.txt', 'w')
    if p==1:
        puntaje.write(str(current1))
        puntaje.write('\n')
        puntaje.write(str(current2))
    else:
        puntaje.write(str(current1))
        puntaje.write(str(current2))
        puntaje.write('\n')
    puntaje.write(max1)
    puntaje.write(max2)
    puntaje.close()

    if int(max1)==int(current1):
        print('Ganó el jugador 1')
        return True
    elif int(max2)==int(current2):
        print('Ganó el jugador 1')
        return True
    else:
        return False