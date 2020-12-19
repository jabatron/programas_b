""" 
Detalles del programa semanal:
Crea un programa que haga una busqueda en google y tome los 3 primeros resultados 
de la busqueda y las muestre en pantalla...

Requerimientos:
1.Hacer busqueda de google y mostrar los 3 primeros resultados
2.Utilizar algun metodo de entrada de texto para que el usuario pueda hacer la 
busqueda de google.

Opcional:
Mostrar un pequeño pedazo del contenido de la web en los resultados 
(como cuando haces una busquesa desde un navegador y ves que tiene de 
contenido desde el pedazo de texto que te muestea google.

Nota: El motor de busqueda puede ser google u otro de tu preferencia (ej: bing, duckgogo, etc)

Programa alternativo:

Programa que imprima unas operaciones matematicas con numeros ingresados por el usuario (5) y 
los imprima 1 cada segundo, mientras en cada operacion ira sumando cada numero ingresado y 
mostrara el avanze...
(Ej: 
1 + 2 = 3
3 + 7 = 10
10 + 1 = 11...)

code: progb_15_tuuser.py
@aprenderpython
#webscraping
"""

# Comprobamos que estan todos modulos instalados
try: 
    from requests import get
    from bs4 import BeautifulSoup
except Exception as e:
    print ("Module requests and bs4 are obligatory to instal")
    print (e)
    print ("Please install module: 'pip install <module>'")

import argparse  

def comprobar_argumentos ():
    parser = argparse.ArgumentParser (description="Búsqueda en google", epilog="@jabaselga")
    parser.add_argument ("-t", "--texto", metavar="Texto busqueda", help="Texto para realizar la busqueda")
    parser.add_argument ("-n", "--num", help="Numero de búsquedas", type=int, choices=range(1, 10))
    parser.add_argument ("-v", "--verbose", help="Muestra mas detalle", type=int, choices=[1, 2, 3], default=2)
       
    args = parser.parse_args() 

    return args 

class Busqueda():
    def __init__ (self, topic, args):
        self.__topic = topic
        self.__num = args.num if args.num else 3
        self.__error = None
        self.__www = []
        self.__descripcion = []
        self.__cabecera = []
        self.__args = args
    
    def buscar (self):
        #URL = f"https://www.google.com/search?q={self.__topic}&num={self.__num}"
        URL = f"https://www.google.com/search?q={self.__topic}&num=12"
        #URL = f"https://www.google.com/search?sxsrf=ALeKk01J4OUE7bgKRN6xNGhYbXc_nbEOow%3A1608219017996&ei=iXnbX_CePJKcgQbr2q2YBA&q={self.__topic}&oq={self.__topic}&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1AAWABgqtABaABwAngAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpesgBCMABAQ&sclient=psy-ab&ved=0ahUKEwiwh6faqtXtAhUSTsAKHWttC0MQ4dUDCA0&uact=5&num=12"
        usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        print (URL)

        try:
            self.__busqueda = get(URL, headers=usr_agent)
        except Exception as e:
            self.__error = e
        else:    
            if self.__busqueda.status_code == 200:
                self.__busqueda_page = self.__busqueda.content
            else:
                self.__error = "An error has occurred."
    # hacer búsqueda

    def extraer (self):
        if not self.__error:
            soup = BeautifulSoup(self.__busqueda_page, 'html.parser')
            busquedas=soup.find_all('div', attrs={'class': 'g'})
            i = 0
            for result in busquedas:
                if i == self.__num:
                    return
                else:
                    i += 1
                link = result.find('a', href=True)
                title = result.find('h3')
                c= result.span.text
                if link and title:
                    self.__cabecera.append (c)
                    # print (c)
                    self.__www.append(link['href'])
                    # print (link['href'])
                    d= result.find('span', attrs={'class': 'aCOpRe'}).text
                    self.__descripcion.append(d)
                    # print (d)
                # print("")
            
    def presentar (self):
        if not self.__error:
            msg = f"Mostrando las {self.__num} primeras busquedas de {self.__topic}."
            print (msg)
            print ("-" * len(msg))
           # print (self.__busqueda.content)
        for i in range(len (self.__www)):
            if self.__args.verbose == 2 or self.__args.verbose == 3:
                print (self.__cabecera[i])
            print (self.__www[i])
            if self.__args.verbose == 3:
                print (self.__descripcion[i])
            print ("")
        print ("")
    # mostrar busqueda

def main ():
    args = comprobar_argumentos()
    if args.texto:
        texto = args.texto
    else:
        texto = input ("Introduzca texto a buscar: ")
    b = Busqueda(texto, args)
    b.buscar()
    b.extraer()
    b.presentar()





if __name__ == "__main__":
    main ()