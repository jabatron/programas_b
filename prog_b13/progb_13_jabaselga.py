""" 
Proyectos y Programas PYTHON
Detalles del programa semanal:

Crea un programa que disponga de varias opciones y estas ayuden al mantenimiento de sistema, ej: borrar archivos basura, borrar cache, borrar archivos de la papelería de reciclaje, borrar archivos duplicados en un directorio, mostrar información del sistema (como ram, procesador, almacenamiento disponible). Nota: Estas opciones pueden ser las que tu consideres que son utiles para el manteminiento asi que puedes buscar otras formas ademas de los expuestos en el ejemplo

Requerimientos:
1.Minimo 4 opciones diferentes (ya sea mediante un menú o argumentos)

2.Mostrar una barra de estado mientras el proceso transcurre y/o mostrar en que parte del proceso esta... (ej: borrando archivos..., borrando carpetas)

3.Mostrar con estetica

4.Puedes elejir si esta herramienta funcionara para windows/linux o en ambos, si se ejecutase en un sistema que no es compatible lo expuesto entonces el programa debe decirte que solo se ejuta en x sistema

Programas completados:


Programa alternativo:

Crea un programa que te imprima cuantos dias faltan para que termine el año desde el dia actual en que se ejecute el programa.

code: progb_13_dcastillo_jabaselga.py
@aprenderpython
#herramientas_sistemas/escritorio


"""

import datetime

def alternativo():
    """
        Calcula los días hasta final de año
    """
    hoy = datetime.datetime.now()
    findeaño = datetime.datetime(hoy.year, 12, 31)
    diferencia = findeaño - hoy

    print (f"Quedan {diferencia.days} hasta final de año.")

if __name__ == "__main__":
    
    alternativo()
