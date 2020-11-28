""" 
Proyectos y Programas PYTHON
Detalles del programa semanal:

Crea un programa que disponga de varias opciones y estas ayuden al mantenimiento de sistema, 
ej: borrar archivos basura, borrar cache, borrar archivos de la papelería de reciclaje, 
borrar archivos duplicados en un directorio, 
mostrar información del sistema (como ram, procesador, almacenamiento disponible). 
Nota: Estas opciones pueden ser las que tu consideres que son utiles para el manteminiento asi 
que puedes buscar otras formas ademas de los expuestos en el ejemplo

Requerimientos:
1.Minimo 4 opciones diferentes (ya sea mediante un menú o argumentos)
2.Mostrar una barra de estado mientras el proceso transcurre y/o mostrar en que parte del proceso esta... (ej: borrando archivos..., borrando carpetas)
3.Mostrar con estetica
4.Puedes elejir si esta herramienta funcionara para windows/linux o en ambos, si se ejecutase en un sistema que no es compatible lo expuesto entonces el programa debe decirte que solo se ejuta en x sistema



Programa alternativo:
Crea un programa que te imprima cuantos dias faltan para que termine el año desde el dia actual en que se ejecute el programa.

code: progb_13_jabaselga.py
@aprenderpython
#herramientas_sistemas/escritorio


"""

import datetime
import argparse
import glob
import os
import platform
from colorama import Fore, init

def alternativo():
    """
        Calcula los días hasta final de año
    """
    hoy = datetime.datetime.now()
    findeaño = datetime.datetime(hoy.year, 12, 31)
    diferencia = findeaño - hoy

    print (f"Quedan {diferencia.days} hasta final de año.")

def delete_files (patron):
    """
        Borra ficheros según una extensión
    """
    files=glob.glob(patron)
    for i in files:
        os.remove(i)

def basic_info():
    usuario = os.getlogin()
    usistema = platform.uname()
    sistema = f"SO: {Fore.GREEN}{usistema[0]}{Fore.RESET}, version {Fore.YELLOW}{usistema[2]}{Fore.RESET} ({usistema[3]})"
    equipo = f"Nombre del equipo: {Fore.CYAN}{usistema[1]}{Fore.RESET}"
    print (f"Ha iniciado sesión con el usuario {Fore.GREEN}{usuario}{Fore.RESET}")
    print (sistema)
    print (equipo)

def borrar_archivos_duplicados(ruta)
    files=glob.glob(ruta)
    duplicados = [item for item, count in collections.Counter(a).items() if count > 1]
    for i in duplicados:
        os.remove()


if __name__ == "__main__":

    parser = argparse.ArgumentParser (description="Help to mantaining syste,", epilog="@jabaselga")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-db", "--deletebak", help="Delete files *.bak.", action="store_true")
    group.add_argument("-bi", "--basicinfo", help="Basic Info System.", action="store_true")
    parser.add_argument("-v", "--verbose", help="Extra info", action="store_true")
    # incluyo el programa ALTERNATIVO - dias hasta fin de año.
    group.add_argument("-a", "--alternative", help="Days before New Years Eve.", action="store_true")

    args = parser.parse_args()   

    # argsn = args.encode or args.decode or args.reverse
    # if not argsn:
    #    parser.error('No arguments to ejecute provided.')

    # colorama inicialización
    init ()

    if args.verbose:
        print (f"{Fore.BLUE}________________________________________________________________________________")
        print ('Ejercicio b12. Codificación/Decodificación e inversión de cadenas.')
        print ('@jabaselga')
        print (f"________________________________________________________________________________{Fore.RESET}")


    if args.alternative:
        alternativo()

    if args.deletebak:
        delete_files("*.bak")
    
    if args.basicinfo:
        basic_info()
