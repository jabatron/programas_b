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

# genero la cadena a usar para codificar
chars64 = string.ascii_uppercase+string.ascii_lowercase+string.digits+'+/'



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


if __name__ == "__main__":

    # leer cadena
    cadena = "Miriam"
    binary = ascii_to_binary (cadena)
    bin64 = binary_to_bin64 (binary)
    hex64 = bin64_to_hex64 (cadena, bin64)

    print (hex64)
