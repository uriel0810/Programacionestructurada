def resolver_mosaico():

    # --- 1. Lectura de Datos ---
    print("Introduce las dimensiones del MOTIVO (filas columnas):")
    try:
        linea1 = sys.stdin.readline().split()
        if not linea1:
            return  # Fin de entrada
        R_motivo, C_motivo = map(int, linea1)
    except ValueError:
        print("Error en formato de dimensiones del motivo.")
        return

    print("Introduce la matriz del MOTIVO:")
    motivo = []
    for _ in range(R_motivo):
        fila = sys.stdin.readline().split()
        if len(fila) != C_motivo:
            print("Error: número incorrecto de columnas en motivo.")
            return
        motivo.append(list(map(int, fila)))

    print("Introduce las dimensiones del MOSAICO (filas columnas):")
    try:
        linea2 = sys.stdin.readline().split()
        R_mosaico, C_mosaico = map(int, linea2)
    except ValueError:
        print("Error en formato de dimensiones del mosaico.")
        return

    print("Introduce la matriz del MOSAICO:")
    mosaico = []
    for _ in range(R_mosaico):
        fila = sys.stdin.readline().split()
        if len(fila) != C_mosaico:
            print("Error: número incorrecto de columnas en mosaico.")
            return
        mosaico.append(list(map(int, fila)))

    # --- 2. Pre-procesamiento del Motivo ---
    puntos_a_verificar = []
    for r in range(R_motivo):
        for c in range(C_motivo):
            if motivo[r][c] != 0:
                puntos_a_verificar.append((r, c, motivo[r][c]))

    # --- 3. Búsqueda ---
    coincidencias = []

    limite_filas = R_mosaico - R_motivo + 1
    limite_cols = C_mosaico - C_motivo + 1

    for r in range(limite_filas):
        for c in range(limite_cols):
            match = True

            for pr, pc, valor in puntos_a_verificar:
                mosaico_r = r + pr
                mosaico_c = c + pc

                if mosaico[mosaico_r][mosaico_c] != valor:
                    match = False
                    break

            if match:
                coincidencias.append((r + 1, c + 1))  # base 1

    # --- 4. Salida de Resultados ---
    print("\n--- RESULTADOS ---")
    print(f"Número de coincidencias: {len(coincidencias)}")
    print("Lista de posiciones (fila, columna):")
    for pos in coincidencias:
        print(f"{pos[0]}, {pos[1]}")

# Ejecutar si es el archivo principal
if __name__ == "__main__":
    resolver_mosaico()
