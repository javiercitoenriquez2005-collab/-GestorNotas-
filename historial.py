
historial = []

print("Simulación de historial de navegación")
print("Escribe el nombre de una página web, 'ATRAS' para retroceder o 'SALIR' para finalizar.")

while True:
    pagina = input("Ingrese una página web o escriba 'ATRAS' o 'SALIR':\n> ").strip()

    if pagina.upper() == "SALIR":
        print("Fin del programa")
        break
    elif pagina.upper() == "ATRAS":
        if historial:
            pagina_removida = historial.pop()
            print(f"Se quitó: {pagina_removida}")
        else:
            print("No hay páginas en el historial para retroceder.")
    else:
        historial.append(entrada)
        print(f"Página visitada: {entrada}")

    print(f"Historial: {historial}")
    print("**" * 40)
