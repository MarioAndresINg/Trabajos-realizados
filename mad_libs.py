print("¡Bienvenido a Mad Libs en Python!")
print("Completa los siguientes campos para crear tu historia:")

nombre = input("Escribe un nombre: ")
lugar = input("Escribe un lugar: ")
animal = input("Escribe un animal: ")
adjetivo = input("Escribe un adjetivo: ")
verbo = input("Escribe un verbo: ")

historia = f"""
Había una vez un(a) {animal} llamado(a) {nombre}.
Un día decidió ir a {lugar} porque queria conocer nuevos lugares por que se sentía  {adjetivo}.
Al llegar, decidió {verbo} y un grupo de leones quedaron sorprendidos.
¡Fue un día inolvidable para {nombre}:
"""
print (historia)