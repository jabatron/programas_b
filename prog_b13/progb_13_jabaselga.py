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


LIBRERIAS ADICIONALES:

pip3 install pstools

"""

import datetime
import argparse
import glob
import os
import getpass
import platform
import shutil
import psutil
from colorama import Fore, init

def alternativo():
    """
        Calcula los días hasta final de año
    """
    hoy = datetime.datetime.now()
    findeaño = datetime.datetime(hoy.year, 12, 31)
    diferencia = findeaño - hoy

    print (f"Quedan {Fore.CYAN}{diferencia.days}{Fore.RESET} días hasta final de año.")

def delete_files (patron):
    """
        Borra ficheros según una extensión
    """
    files=glob.glob(patron)
    for i in files:
        os.remove(i)

def delete_cache ():
    """
        Borra ficheros según una extensión
    """
    path = "/home/"+getpass.getuser()+"/.cache2/**"
    files = glob.glob(path, recursive=False)
    
    for i in files:
        try:
            shutil.rmtree(i)
        except:
            os.remove(i)

def matar_proceso (proceso):

    process = False
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == proceso:
            proc.kill()
            process = True
            
    if process:
        print ("Proceso matado")
    else:
        print ("Proceso no encontrado")

def basic_info():
    #   usuario = os.getlogin()
    usuario = getpass.getuser()
    usistema = platform.uname()
    sistema = f"SO: {Fore.GREEN}{usistema[0]}{Fore.RESET}, version {Fore.YELLOW}{usistema[2]}{Fore.RESET} ({usistema[3]})"
    equipo = f"Nombre del equipo: {Fore.CYAN}{usistema[1]}{Fore.RESET}"
    mem = psutil.virtual_memory()
    memoria = round (mem.total/(1024*1024*1024), 2)
    disco=psutil.disk_usage('/')
    print (f"Ha iniciado sesión con el usuario {Fore.GREEN}{usuario}{Fore.RESET}")
    print (sistema)
    print (equipo)
    print (f"Hay {Fore.GREEN}{memoria} Gb{Fore.RESET} de RAM y el disco esta ocupado al {Fore.GREEN}{disco.percent}%{Fore.RESET}.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser (description="Help to mantaining syste,", epilog="@jabaselga")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-db", "--deletebak", help="Delete files *.bak.", action="store_true")
    group.add_argument("-dc", "--deletecache", help="Delete files in cache.", action="store_true")
    group.add_argument("-bi", "--basicinfo", help="Basic Info System.", action="store_true")
    group.add_argument("-kp", "--killprocess", help="Kill a process.")
    parser.add_argument("-v", "--verbose", help="Extra info", action="store_true")
    # incluyo el programa ALTERNATIVO - dias hasta fin de año.
    group.add_argument("-a", "--alternative", help="Days before New Years Eve.", action="store_true")

    args = parser.parse_args()   

    
    if not (args.deletebak or args.deletecache or args.basicinfo or args.killprocess):
        parser.error('No arguments to ejecute provided.')

    # colorama inicialización
    init () 

    if args.verbose:
        print (f"{Fore.BLUE}________________________________________________________________________________")
        print ('Ejercicio b13. Mantenimiento del sistema.')
        print ('@jabaselga')
        print (f"________________________________________________________________________________{Fore.RESET}")


    if args.alternative:
        alternativo()

    if args.deletebak:
        delete_files("*.bak")
    
    if args.basicinfo:
        basic_info()

    if args.deletecache:
       delete_cache()

    if args.killprocess:
        matar_proceso(args.killprocess)