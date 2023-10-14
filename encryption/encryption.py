from cryptography.fernet import Fernet

# Función para generar una clave aleatoria
def generar_clave():
    clave = Fernet.generate_key()  # Genera una clave Fernet aleatoria
    with open("clave.key", "wb") as clave_archivo:  # Abre un archivo binario para guardar la clave
        clave_archivo.write(clave)  # Escribe la clave en el archivo
    return clave

# Función para cargar una clave desde un archivo
def cargar_clave():
    with open("clave.key", "rb") as clave_archivo:  # Abre el archivo binario que contiene la clave
        clave = clave_archivo.read()  # Lee la clave desde el archivo
    return clave

# Función para encriptar un mensaje
def encriptar_mensaje(mensaje, clave):
    fernet = Fernet(clave)  # Crea un objeto Fernet con la clave proporcionada
    mensaje_encriptado = fernet.encrypt(mensaje.encode())  # Encripta el mensaje
    return mensaje_encriptado

# Función para desencriptar un mensaje
def desencriptar_mensaje(mensaje_encriptado, clave):
    fernet = Fernet(clave)  # Crea un objeto Fernet con la clave proporcionada
    mensaje = fernet.decrypt(mensaje_encriptado).decode()  # Desencripta el mensaje y lo convierte en texto
    return mensaje

# Ejemplo de uso
if __name__ == "__main__":
    clave = None

    while True:
        opcion = input("¿Desea generar una nueva clave (g), utilizar una existente (e), encriptar (en) o desencriptar (de) un mensaje?: ").strip().lower()

        if opcion == "g":
            clave = generar_clave()
            print("Clave generada y guardada en 'clave.key'")
        elif opcion == "e":
            clave = cargar_clave()
            print("Clave cargada desde 'clave.key'")
        elif opcion == "en":
            if clave is not None:
                mensaje = input("Ingrese el mensaje a encriptar: ")
                mensaje_encriptado = encriptar_mensaje(mensaje, clave)
                print(f"Mensaje encriptado: {mensaje_encriptado}")
            else:
                print("Primero debe generar o cargar una clave.")
        elif opcion == "de":
            if clave is not None:
                mensaje_encriptado = input("Ingrese el mensaje encriptado: ")
                mensaje_desencriptado = desencriptar_mensaje(mensaje_encriptado.encode(), clave)
                print(f"Mensaje desencriptado: {mensaje_desencriptado}")
            else:
                print("Primero debe generar o cargar una clave.")
        else:
            print("Opción no válida. Use 'g' para generar una clave, 'e' para cargar una clave, 'en' para encriptar o 'de' para desencriptar un mensaje.")