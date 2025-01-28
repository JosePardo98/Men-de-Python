def suma_numeros():
    n = int(input("¿Cuántos números deseas sumar? "))
    total = 0
    for i in range(n):
        num = float(input(f"Ingresa el número {i+1}: "))
        total += num
    print(f"La suma total es de: {total}")

def producto_numeros():
    n = int(input("¿Cuántos números deseas multiplicar? "))
    total = 1
    for i in range(n):
        num = float(input(f"Ingresa el número {i+1}: "))
        total *= num
    print(f"El producto total es: {total}")

def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Suma de 'n' números")
    print("2. Producto entre 'n' números")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-3): ")

        if opcion == '1':
            suma_numeros()
        elif opcion == '2':
            producto_numeros()
        elif opcion == '3':
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 3.")

if __name__ == "__main__":
    main()
