#!/usr/bin/python3
""" 
Detalles del programa semanal:

Crea un programa para descargar archivos de repositorios de GitHub. 

Requerimientos:
1.La URL la ingresa el usuario y luego el programa descargara el código de ese archivo 
sin tener que descargar todo el repo.

2. Guardar lo descargado en el directorio actual o configurar una opción para que el 
usuario elija donde descargarlo.

Opcional:
Tener la opción de descargar todo el repositorio

Programa alternativo:
°Crea un programa que tenga una funcion que imprima un nombre un numero de veces 
especificados por el usuario, la funcion debe contener 2 parametros que son:
1: un nombre introducido por el usuario, 
2: la cantidad de veces que se imprimira ese nombre

code: progb_16_tuuser.py
@aprenderpython
#webscraping

https://github.com/AprenderPython/programas_b/blob/master/prog_b12/prog_b12_Raul.py
https://raw.githubusercontent.com/AprenderPython/programas_b/master/prog_b12/prog_b12_Raul.py
"""

# Comprobamos que estan todos modulos instalados
import sys
import re
import os
try: 
    from requests import get
    from bs4 import BeautifulSoup
except Exception as e:
    print ("Module requests and bs4 are obligatory to instal")
    print (e)
    print ("Please install module: 'pip install <module>'")
    sys.exit ()

import argparse
import urllib.parse
from colorama import Fore, init

def comprobar_argumentos ():
    parser = argparse.ArgumentParser (description="Búsqueda en google", epilog="@jabaselga")
    parser.add_argument ("-t", "--texto", metavar="Texto busqueda", help="Texto para realizar la busqueda")
    parser.add_argument ("-d", "--directorio", help="Numero de búsquedas")
    parser.add_argument ("-r", "--repo", help="Numero de búsquedas")
    parser.add_argument ("-v", "--verbose", help="Muestra mas detalle", type=int, choices=[1, 2, 3], default=2)
       
    args = parser.parse_args() 

    return args 

def comprobar_url (url):
    m = re.search ('^https://(www\.)?github.com', url)
    if not m:
        print ("No es una dirección de github -> 'https://github.com/usuario/...")
        return None
    else:
        return url

def check_ruta (ruta):
    print (ruta)
    r = os.path.isdir (ruta)
    r_w = os.access (ruta, os.W_OK)

    return r, r_w

def github_raw (url):
    rurl=url.replace("github.com","raw.githubusercontent.com")
    rurl=rurl.replace ("blob/","")
    return rurl

def github_download_file(rurl, ruta=None):
    r = get(rurl)
    if ruta:
        c_r, c_rw = check_ruta(ruta)

    if r.status_code == 200:
        *_, filename = rurl.split ('/')
    
        fichero = open (ruta+"\\"+filename, 'wb')
        fichero.write(r.content)
        fichero.close ()
    else:
        print ("URL erronea, compruebe USUARIO, FICHERO y RUTA")
        sys.exit ()

def descargar_repo (url, ruta):
    
    new_url, _= url.split("blob")
    page=get(new_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all('a'):
        h = link.get('href')
        
        if "zip" in h:
            ruta_zip = f"https://github.com/{h}" 
    print (ruta_zip)
    *_, filename = ruta_zip.split ("/")

    fullname = f"{ruta}/{filename}"
    
    r = get(new_url, stream=True)
    with open(fullname, 'wb') as fd:
        fd.write(r.content)

def main ():
    args = comprobar_argumentos()
    if args.verbose == 3:
        print (f"{Fore.BLUE}________________________________________________________________________________")
        print ('Ejercicio b16. Descargas de archivos de github.')
        print ('@jabaselga')
        print (f"________________________________________________________________________________{Fore.RESET}")


# Comprobamos URL
    if args.texto:
        url = args.url
    else:
        url = input ("Introduzca la URL del fichero a descargar: ")
        url = comprobar_url(url)
    
    if url:
        url_raw = github_raw (url)
        print (url_raw)
    else:
        print ("URL erronoea")
        sys.exit ()

# Comprobamos DIRECTORIO
    if args.directorio:
        ruta = args.directorio
    else:
        ruta = input ("Introduce la ruta para descargar el fichero. (VACIO para ruta actual): ")
        if ruta.strip() == "":
            ruta = os.getcwd()

    r, rw = check_ruta (ruta)

# Descargar fichero y grabar
    if r and rw:
        github_download_file (url_raw, ruta)
    else:
        print ("Problemas para guardar el fichero")
        sys.exit ()

# Descargar todo el repositorio

    if args.repo:
        todo = args.repo
    else:
        todo = input ("¿Quieres descargar todo el repositorio?")

    if todo:
        descargar_repo (url, ruta)

if __name__ == "__main__":
    main ()