print("primera calculadora")
# mi primera calculadora en Python
# calculadora.py            
def sumar(a, b):
    """Suma dos números."""
    return a + b
def restar(a, b):
    """Resta dos números."""
    return a - b
def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b
def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def main():
    print("ingrese dos números para realizar una operación:")
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Seleccione una opción (1-4): ")
    
    if opcion in ['1', '2', '3', '4']:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            resultado = sumar(a, b)
        elif opcion == '2':
            resultado = restar(a, b)
        elif opcion == '3':
            resultado = multiplicar(a, b)
        elif opcion == '4':
            resultado = dividir(a, b)
        
        print(f"El resultado es: {resultado}")
    else:
        print("Opción no válida.")
if __name__ == "__main__":
    main()
    # fin del programa
    #Hecho por Mario Andres Garavito
    # Fecha: 2023-10-014