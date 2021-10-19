from funciones import tradletra, cualp, readMaxPoints

def largos(inicio, fin, p):
    d = open('data.txt','r')
    linea=d.readline()
    if p==2:
        linea=d.readline()
    temp=d.readline()
    linea=list(linea)
    
    if int(inicio/10)==int(fin/10):         #horizontal
        inicio*=2
        fin=(fin+1)*2
        points=(((fin/2)-1) -(inicio/2)) +1
        for i in range(inicio, fin, 2):
            linea[i]='X'
        
    elif inicio%10==fin%10:                 #vertical
        inicio*=2
        fin*=2
        points=((fin-inicio))/20 +1
        for i in range(inicio, fin+1, 20):
            linea[i]='X'
    
    else:
        print('Dejese de cosas y ponga coordenadas bien')
    readMaxPoints(p, int(points))

    line=''
    for i in linea:
        line += i
    d.close()
    
    return line, temp
        
def main():
    datos = open('data.txt', 'w')    #cuadricula vacia
    for k in range(4):
        for i in range(10):
            for j in range(10):
                datos.write('- ')
        datos.write('\n')
    datos.close()

    while True:                      #crear barcos
        jugador=int(input('Jugador: '))
        intro=input('Inicio del barco: ')
        inicio=int(intro[1:])*10+tradletra(intro[0])
        intro=input('Fin del barco: ')
        fin=int(intro[1:])*10+tradletra(intro[0])

        cuad=largos(inicio,fin, jugador)
        cualp(cuad[0], cuad[1], jugador)

        if input('Continuar? ')=='no':
            break
main()