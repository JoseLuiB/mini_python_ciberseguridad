import socket

# Solicita al usuario que ingrese la dirección IPv4 a escanear
ip = input("Ingrese la dirección IPv4 a escanear: ")

try:
    # Resuelve la dirección IP para evitar problemas de resolución de nombres
    target_ip = socket.gethostbyname(ip)

    for puerto in range(1, 65536):  # Escaneamos puertos del 1 al 65535
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Establecemos un tiempo de espera de 1 segundo

            resultado = sock.connect_ex((target_ip, puerto))

            if resultado == 0:
                print(f"El puerto {puerto} está abierto")
            else:
                print(f"Puerto {puerto} filtrado o puerto cerrado")

except socket.gaierror:
    print("La dirección IP ingresada no es válida.")
except KeyboardInterrupt:
    print("Escaneo interrumpido por el usuario.")

print("Escaneo de puertos finalizado.")
