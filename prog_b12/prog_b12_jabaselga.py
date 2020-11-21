""" 
Detalles Programa semanal:

Crea un programa que mediante argumentos (ej; python archivo.py argumento) pueda convertir de texto a base64 y viceversa.

Requerimientos:

°Determinar si es texto plano o base64 para luego imprimir la conversion, puede ser mediante argumentos, ej: -texto o -base64, (o como gusten)
°Imprimir el resultado de la conversion.

Programas completados::white_check_mark:
°Ecotracker: Ver programa
°Raul: Ver programa  

Programa alternativo:

Crea un programa que te pregunte tu nombre y luego te lo imprima alrevez, ej: carlos > solrac

code: progb_12_tuuser.py
@aprenderpython
#criptografia




"""

import string
import re
import argparse


# genero la cadena a usar para codificar
chars64 = string.ascii_uppercase+string.ascii_lowercase+string.digits+'+/'
# creo un diccionario para las búsquedas inversas
dict_chars64 = {i:j for j,i in enumerate(chars64)}


def ascii_to_binary(cadena):
    """ 
        Devuelve una lista de string de la conversión en binario de la cadena
        ajustdo con ceros por la izquierda si tiene menos de longitud 8
    """
    cadena_bin = [bin(ord(i))[2:] for i in cadena]
    for i in range(len(cadena_bin)):
        cadena_bin[i]='0'*(8-len(cadena_bin[i]))+cadena_bin[i]

    cadena_sum =""
    
    for s in cadena_bin:
        cadena_sum+=s
    
    return cadena_sum

def binary_to_bin64(cadena_bin):
    """ 
        Reorganizar la cadena binaria pasando de grupos de 8 a grupos de 6
    """
    # Trocear la cadena en grupos de 6
    lb=re.findall(".{1,6}", cadena_bin)
    # Si el último grupo no tiene 6 digitos se rellena con "0"
    lb[-1]=lb[-1]+"0"*(6-len(lb[-1]))

    return lb

def calculate_fill(cadena):
    """ 
        Si la cadena no es multiplo de 3 se rellena con "="
        Devuelve la cantidad de "=" que se necesitan para completar la codificación
    """
    return  (3-len(cadena)%3)%3

def bin64_to_hex64(cadena, cadena_bin):
    """ 
        Convierte la cadena bin64 a la codificacion hex64. 
        Añade los correspondientes "=" si la cadena no es multiplo de 3 bytes
    """
    cadena_hex64=""
    for i in cadena_bin:
        cadena_hex64+=chars64[int(i, 2)]
        
    cadena_hex64+= ('='*calculate_fill(cadena))

    return cadena_hex64


def cadena64_to_dig64(cadena64):
    """ 
        convierte la cadena a su valor decimal correspondiente.
        elimina los "=" del final.
    """
    ld=[]
    for i in cadena64:
        if i != '=':
            ld.append(dict_chars64[i])
    
    return ld

def dig64_to_bin6(dig):

    cadena_bin= [bin(i)[2:] for i in dig]
    for i in range(len(cadena_bin)):
        cadena_bin[i]='0'*(6-len(cadena_bin[i]))+cadena_bin[i]

    cadenasum=""
    for i in cadena_bin:
        cadenasum+=i

    la=re.findall(".{1,8}", cadenasum)

    if len(la[-1])<8:
        la.pop()

    return la

def bin6_to_ascii(la):
    cad=""
    for i in la:
        cad+=chr(int(i,2))

    return cad


def string_to_base64(cadena):

    binary = ascii_to_binary (cadena)
    bin64 = binary_to_bin64 (binary)
    hex64 = bin64_to_hex64 (cadena, bin64)

    return hex64

def base64_to_string(base64):
    dig64 = cadena64_to_dig64(base64)
    bin6 = dig64_to_bin6(dig64)
    cadena=bin6_to_ascii(bin6)

    return cadena


def string_reverse(cadena):
    return cadena[::-1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser (description="Code/Decode base64 and reverse string", epilog="@jabaselga")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--encode", metavar="string", help="String to encode.")
    group.add_argument("-d", "--decode", metavar="string", help="String to decode.")
    group.add_argument("-r", "--reverse", metavar="string", help="String to reverse.")
    
    args = parser.parse_args()   

    argsn = vars(parser.parse_args())
    if not any(argsn.values()):
        parser.error('No arguments provided.')

    if args.encode:
        base64 = string_to_base64(args.encode)
        print (base64)
    if args.decode:
        cadena = base64_to_string(args.decode)
        print (cadena)

    # extra: programa alternativo
    if args.reverse:
        cr = string_reverse(args.reverse)
        print (cr)