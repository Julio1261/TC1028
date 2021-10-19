from funciones import checkwin, ver, tradletra, cualp

def play(p):
    if p==2:
        p=1
    else:
        p=2

    while True:
        if checkwin(p, 0):
            print('El juego se terminó.')
            break
        d = open('data.txt','r')
        linea=d.readline()
        
        if p==2:
           linea=d.readline() 
        else:
            lineamostrada=d.readline()
        lineamostrada=d.readline()
        if p==2:
            lineamostrada=d.readline()

        linea=list(linea)
        lineamostrada=list(lineamostrada)
        intro=input('Coordenada: ')
        coo=(int(intro[1:])*10+tradletra(intro[0]))*2

        if linea[coo]=='X':
            linea[coo]='U'
            lineamostrada[coo]='X'
            print('Hit!')
            checkwin(p, 1)
                
        elif linea[coo]=='-':
            linea[coo]='O'
            lineamostrada[coo]='O'

        line=''
        most=''
        for i in linea:
            line += i
        for i in lineamostrada:
            most += i

        d.close()
        cualp(line, most, p)
        ver(p)

        if linea[coo]!='U':
            print('Te equivocaste. Se acabó tu turno.')
            break

turn = open('turno.txt', 'r')
player=int(turn.readline())
turn.close()
quien=input('¿Quién eres? ')

if (quien=='Julio' and player==1) or (quien=='Karla' and player==2):
    play(player)
    turn = open('turno.txt', 'w')
    if player==1:
        turn.write('2')
    else:
        turn.write('1')
    turn.close()
else:
    print('No es tu turno.')