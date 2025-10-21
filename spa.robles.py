# Simulador SPA ROBLES
# Curso: Estrutura de datos
# Nombre del estudiante: Mario Andres Garavito

def mostrar_informacion_inicial():
    print("=======================================")
    print("        Simulador SPA ROBLES")
    print("        Curso: estrutura de datos")
    print("        Estudiante: Mario Andres Garavito")
    print("=======================================\n")

def verificar_contraseña():
    contraseña_correcta = "123"
    intentos = input("Ingrese la contraseña para acceder al sistema: ")
    if intentos == contraseña_correcta:
        return True
    else:
        print("Contraseña incorrecta. Acceso denegado.")
        return False
     
def selecionar_servicios():
    print("n\ Servicios disponibles:")
    print("1. corte y cepillado - $60,000")
    print("2. corte, cepillado y Uñas - $90,000")
    print("3. Uñas en acrilico y cejas - $100,000")
    print("4. Uñas en acrilico,maquillaje y cejas - $140,000")
    opcion = input("selecione el numero de servicio que deseas: ")
    servicios = {
        "1": ("Corte y cepillado", 60000),
        "2": ("Corte, cepillado y uñas", 90000),
        "3": ("Uñas en acrílico y cejas", 100000),
        "4": ("Uñas en acrílico, maquillaje y cejas", 140000)
    }
    servicios = servicios.get(opcion)
    if servicios:
        return servicios
    else:
        print("Opción no válida. Por favor, seleccione un servicio válido.")
        return selecionar_servicios()
    
def calcular_descuento(estrato):
    estrato = int(estrato)
    if estrato in [1, 2]:
        return 0.15
    elif estrato in [3, 4]:
        return 0.10
    elif estrato >= 5:
        return 0.05
    else:
        print("Estrato no válido. se aplicara un descuento del 0%.")
        return 0

def main():
    mostrar_informacion_inicial()
    if not verificar_contraseña():
        return

    # Ingreso de datos del usuario
    print("\nIngrese los datos del usuario:")
    cedula = input("Cédula: ")
    nombre = input("Nombre completo: ")
    estrato = input("Estrato socioeconómico (número): ")
    servicio_nombre, valor_servicio = selecionar_servicios()

    # Cálculo del descuento
    porcentaje_descuento = calcular_descuento(estrato)
    descuento = valor_servicio * porcentaje_descuento
    valor_a_pagar = valor_servicio - descuento

    # Mostrar resultados
    print("\n----- RESULTADO -----")
    print(f"Identificación (Cédula): {cedula}")
    print(f"Nombre completo: {nombre}")
    print(f"Servicio utilizado: {servicio_nombre}")
    print(f"Estrato socioeconómico: {estrato}")
    print(f"Valor a pagar: ${valor_a_pagar:,.0f}")
    print(f"Descuento obtenido: ${descuento:,.0f}")
   
if __name__ == "__main__":
    main()