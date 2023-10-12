# Importación de librerías
import requests  # Para realizar consultas y peticiones a sitios web
from os import path  # Para comprobar la existencia de rutas de archivos
import argparse  # Para agregar argumentos a la hora de la ejecución del programa
import sys  # Para funcionalidades adicionales del sistema

# Crear un analizador de argumentos con una descripción
parser = argparse.ArgumentParser(description="Encuentra subdominios en un dominio víctima.")
# Agregar un argumento requerido para el dominio objetivo
parser.add_argument("-t", "--target", required=True, help="Dominio víctima")
# Analizar los argumentos proporcionados por el usuario
args = parser.parse_args()

def main():
    if path.exists("subdominios.txt"):
        # Abrir y leer el archivo "1_subdominios.txt" con subdominios separados por saltos de línea
        wordlist = open("subdominios.txt", "r").read().split("\n")
        
        for i in wordlist:
            for protocol in ["http://", "https://"]:
                # Construir una URL combinando el protocolo, el subdominio y el dominio objetivo
                url = f"{protocol}{i}.{args.target}"
                try:
                    # Realizar una solicitud web y obtener la respuesta
                    response = requests.get(url)
                    response.raise_for_status()  # Lanzar una excepción si la respuesta no es exitosa
                    print(f"( * ) Subdominio encontrado: {url} ( * )")
                except (requests.exceptions.RequestException, requests.ConnectionError):
                    # Ignorar errores de conexión y solicitudes no exitosas
                    pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
