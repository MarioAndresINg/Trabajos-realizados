#vamos hacer una generador de contraseñas
import random
import string
def generar_contraseña(longitud):
    caracteres = string.ascii_letters +string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña 
if __name__ == "__main__":
    while True:
        
     longitud = int(input("Ingrese la longitud de la contraseña: "))
     contraseña = generar_contraseña(longitud)
     print(f"Contraseña generada: {contraseña}")
     respuesta = input("¿Desea generar otra contraseña? (si/no): ")
     if respuesta == "si":
        break
     print("Gracias por usar el generador de contraseñas. ¡Hasta luego!")
# Hecho por Mario Andres Garavito