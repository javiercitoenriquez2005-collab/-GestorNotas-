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

