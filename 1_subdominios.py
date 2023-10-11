#importacion de libreriras
import requests #consutas y peticiones a sitios web
from os import path #comprobar existencia de rutas
import argparse #poder agregar parametros a la hora de ejecucion
import sys #funcionalidades adicionales

#creamos una variable
parser = argparse.ArgumentParser()
#agregamos un argumento
parser.add_argument("-t", "--target", help="Indica el dominio victima")
#pasar el argumento a la variable parser
parser = parser.parse_args()

def main():
    pass



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()