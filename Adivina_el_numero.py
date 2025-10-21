print("Adivina el número")
# Adivina el numero primera version en Python
import random

print("¡Bienvenido al juego de Adivina el Número!")
numero_secreto = random.randint(1,100)
intentos =0

while True:
    intentos=int(input("Adivina un número entre 1 y 100: "))
    intentos +=1
    if intentos < numero_secreto:
        print("demasiado bajo, intenta de nuevo")
    elif intentos > numero_secreto:
        print("demasiado alto, intenta de nuevo")
    else:
        print(f"felicidades has adivinado el numero  en {intentos} intentos")
        break
    print("Si quieres salir del juego, escribe 'salir'")
    if intentos == 'salir':
        print("Gracias por jugar. ¡Hasta luego!")
        break
# Hecho por Mario Andres Garavito
# Fecha: 2023-10-014

