import subprocess
import argparse

def main():
    # Configuración de argumentos de línea de comandos
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", help="Indica la URL")
    args = parser.parse_args()

    if args.target:
        try:
            # Ejecuta el comando "wad" para obtener información sobre las tecnologías en la URL objetivo
            result = subprocess.check_output(["wad", "-u", args.target], text=True)
        except subprocess.CalledProcessError:
            print("Error al ejecutar el comando 'wad'")
            return

        # Busca la información de tecnologías entre corchetes en la salida del comando
        start_index = result.find("[")
        end_index = result.find("]", start_index)

        if start_index != -1 and end_index != -1:
            tecnologias = result[start_index + 1:end_index]
            
            # Abre un archivo para escritura y escribe las tecnologías encontradas
            with open("tecnologias.txt", "w") as file:
                file.write(tecnologias)
            
            print("Tecnologías encontradas:", tecnologias)
        else:
            print("No se encontraron tecnologías en la URL proporcionada.")
    else:
        print("Ingresa una URL")

if __name__ == "__main__":
    main()