import string
import random

while True:
    try:
        # Solicita al usuario ingresar la longitud deseada de la contraseña
        longitud = int(input("Ingresa la longitud deseada de la contraseña (entre 8 y 25 caracteres): "))
        
        if 8 <= longitud <= 25:
            # Si la longitud está dentro del rango válido, sal del bucle
            break
        elif longitud < 0:
            # Si la longitud es negativa, muestra un mensaje de error
            print("La longitud no puede ser un número negativo. Por favor, intenta nuevamente.")
        else:
            # Si la longitud no está en el rango válido, muestra un mensaje de error
            print("La longitud debe estar entre 8 y 25 caracteres.")
    except ValueError:
        # Si se ingresa un valor no numérico, muestra un mensaje de error
        print("Por favor ingrese una longitud numérica válida.")

# Define los caracteres posibles para la contraseña
caracteres = string.ascii_letters + string.digits + string.punctuation

# Genera la contraseña aleatoria usando los caracteres definidos y la longitud ingresada
contraseña = "".join(random.choice(caracteres) for i in range(longitud))

# Abre un archivo "password.txt" en modo escritura y escribe la contraseña en él
with open("password.txt", "w") as file:
    file.write(contraseña)

# Muestra la contraseña generada al usuario
print(f"""Tu contraseña generada es: "{contraseña}" """)
