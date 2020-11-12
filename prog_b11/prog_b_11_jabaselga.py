#/usr/bin/python3
""" 
Detalles Programa semanal:

Crea un programa que via argumentos lea un documento de texto e imprima en pantalla cuantas lineas tiene y el nombre del archivo

Requerimientos:
°Imprimir en pantalla numero de lineas del archivo de texto
°Imprimir el nombre del archivo antes.
°Mostrar con algo de estetica el resultado.

PS > python .\prog_b_11_jabaselga.py
usage: prog_b_11_jabaselga.py [-h] path/filename.ext [path/filename.ext ...]
prog_b_11_jabaselga.py: error: the following arguments are required: path/filename.ext


"""

import argparse
from pathlib import Path

num=[[' ###',' #',' ###',' ###',' # #',' ###',' ###',' ###',' ###',' ###'], 
     [' # #',' #','   #','   #',' # #',' #  ',' #  ','   #',' # #',' # #'], 
     [' # #',' #',' ###',' ###',' ###',' ###',' ###','   #',' ###',' ###'], 
     [' # #',' #',' #  ','   #','   #','   #',' # #','   #',' # #','   #'], 
     [' ###',' #',' ###',' ###','   #',' ###',' ###','   #',' ###',' ###']]

def print_num(num, n):
    numbers=[int(i) for i in str(n)]
    for i in range(5):
        for j in range(len(numbers)):
            print(num[i][numbers[j]], end="")
        print ('')

def file_exist (file):
    """
    comprueba si la ruta/fichero existe
    """
    cf = Path(file)
    if cf.is_file ():
        # El fichero existe
        return True
    else:
        return False

def contarlineas (file):
    return len(open(file, 'rb').readlines(  ))


if __name__ == "__main__":

    #Gestion de argumentos
    parser = argparse.ArgumentParser (description='Count lines in a text file.')
    parser.add_argument ('file', metavar='path/filename.ext', type=str, nargs='+', help='Files to count lines')

    args = parser.parse_args()
    files = (getattr(args, 'file'))

    for f in files:
        #Existe filename
        if file_exist (f):
            #Contar lineas
            print (f'El fichero {f} tiene:')
            print_num (num, (contarlineas (f)))
            print ("LINEAS\n\n")
        else:
            print (f'El fichero {f} no existe o ruta erronea.\n')


    #Mostrar Resultado