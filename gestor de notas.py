def promedionotas(n1, n2, n3):
    """Calcula el promedio de tres notas."""
    return (n1 + n2 + n3) / 3

def leernotas():
    """Solicita al usuario tres notas válidas entre 0 y 100."""
    while True:
        try:
            n1 = int(input("Ingrese nota 1 (0..100): "))
            if 0 <= n1 <= 100:
                break
            else:
                print("Nota fuera de rango.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    
    while True:
        try:
            n2 = int(input("Ingrese nota 2 (0..100): "))
            if 0 <= n2 <= 100:
                break
            else:
                print("Nota fuera de rango.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    
    while True:
        try:
            n3 = int(input("Ingrese nota 3 (0..100): "))
            if 0 <= n3 <= 100:
                break
            else:
                print("Nota fuera de rango.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")
    
    return n1, n2, n3

def Ganando():
    """Algoritmo principal para calcular promedios de estudiantes."""
    try:
        n = int(input("Ingrese la cantidad de alumnos: "))
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        return

    for i in range(1, n + 1):
        print(f"\n--- Estudiante {i} ---")
        n1, n2, n3 = leernotas()
        promindi = promedionotas(n1, n2, n3)
        print(f"Estudiante {i} promedio: {promindi:.2f}")

# Ejecutar el algoritmo
Ganando()
def gestor_notas():
    op = 0

    while op != 5:
        print("\n----- Menú Gestor de Notas Académicas - UMG -----")
        print("1. Registrar un nuevo curso y nota")
        print("2. Mostrar todas las notas")
        print("3. Modificar la nota de un curso")
        print("4. Eliminar un curso y su nota")
        print("5. Salir del sistema")
        
        try:
            op = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número del 1 al 5.")
            continue

        if op == 1:
            print("<Registrar un nuevo curso y nota>")
            # acción aquí
        elif op == 2:
            print("<Mostrar todas las notas>")
            # acción aquí
        elif op == 3:
            print("<Modificar la nota de un curso>")
            # acción aquí
        elif op == 4:
            print("<Eliminar un curso y su nota>")
            # acción aquí
        elif op == 5:
            print("Saliendo del sistema...")
        else:
            print("Opción inválida, intente nuevamente.")

# Ejecutar el menú
gestor_notas()

