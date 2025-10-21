def contar_letras(texto, letras):
    """cuenta la cantidad de veces que aparecen ciertas letras en un texto."""
     
    contador = 0
    for letra in texto:
        if letra.lower() in letras:
            contador += 1       
    return contador
frase = input("Introduce una frase: ")
letra = input("Introduce una letra o varias letras a contar: ")
resultado = contar_letras(frase, letra)
print(f"La cantidad de letras '{letra}' en la frase es: {resultado}")

