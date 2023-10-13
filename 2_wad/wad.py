#Importamos librerias
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="Indica la URL ")
parser = parser.parse_args()

def main():
    if parser.target:
        subprocess.call("wad -u"+parser.target+"> tecnologias.txt", shell=True)
        tecnologias = open("tecnologias.txt", "r")
        tecnologias = tecnologias.read()
        tecnologias = tecnologias.split("[")
        tecnologias = tecnologias[1].split("]")
    else:
        print("Ingresa una URL")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt():
        exit()