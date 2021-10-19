def main():
    datos = open('data.txt', 'w')    #cuadricula vacia
    for k in range(4):
        for i in range(10):
            for j in range(10):
                datos.write('- ')
        datos.write('\n')
    datos.close()
main()