# -----------------------------------------------------------
# Problema: Encender luces en rojo (Turning Red)
# Cada luz puede estar en 3 estados: R=0, G=1, B=2 (mod 3)
# Cada botón suma +1 al estado de las luces que controla.
# Objetivo: lograr que todas las luces queden en 0 (rojo)
# usando el mínimo número de pulsaciones.
# -----------------------------------------------------------

def gauss_mod3(A, b):
    """
    Resuelve el sistema A*x = b (mod 3) usando eliminación de Gauss.
    Regresa (tiene_solucion, vector_x)
    Si no tiene solución, devuelve (False, None)
    """
    n = len(A)
    m = len(A[0])

    row = 0
    for col in range(m):
        # Buscar pivote
        pivot = -1
        for i in range(row, n):
            if A[i][col] % 3 != 0:
                pivot = i
                break

        if pivot == -1:
            continue

        # Intercambiar filas
        A[row], A[pivot] = A[pivot], A[row]
        b[row], b[pivot] = b[pivot], b[row]

        # Normalizar el pivote (hacerlo = 1)
        inv = {1: 1, 2: 2}[A[row][col] % 3]  # inversos modulo 3
        for j in range(col, m):
            A[row][j] = (A[row][j] * inv) % 3
        b[row] = (b[row] * inv) % 3

        # Eliminar en otras filas
        for i in range(n):
            if i != row and A[i][col] != 0:
                factor = A[i][col]
                for j in range(col, m):
                    A[i][j] = (A[i][j] - factor * A[row][j]) % 3
                b[i] = (b[i] - factor * b[row]) % 3

        row += 1

    # Verificar inconsistencia
    for i in range(n):
        if all(A[i][j] == 0 for j in range(m)) and b[i] != 0:
            return (False, None)

    # Extraer solución (variables libres = 0)
    x = [0] * m
    for i in range(n):
        pivot_col = None
        for j in range(m):
            if A[i][j] == 1:
                pivot_col = j
                break
        if pivot_col is not None:
            x[pivot_col] = b[i]

    return (True, x)


def color_to_num(c):
    return {"R": 0, "G": 1, "B": 2}[c]


def main():
    # Leer datos
    l, b = map(int, input("Luces y botones: ").split())
    estado = input("Estados R/G/B: ").strip()

    # Convertir colores a números 0,1,2
    start = [color_to_num(c) for c in estado]

    # Matriz A (luz x botón)
    A = [[0] * b for _ in range(l)]

    for j in range(b):
        datos = list(map(int, input(f"Botón {j+1}: ").split()))
        k = datos[0]
        luces = datos[1:]
        for luz in luces:
            A[luz - 1][j] = 1  # botón j afecta luz luz-1

    # Queremos resolver:
    # A * x = (-start) mod 3
    rhs = [(-start[i]) % 3 for i in range(l)]

    # Copiar para no dañar A
    A2 = [fila[:] for fila in A]
    rhs2 = rhs[:]

    ok, sol = gauss_mod3(A2, rhs2)

    if not ok:
        print("impossible")
        return

    # Mínimo número de pulsaciones: suma de x[j]
    print(sum(sol))


# Ejecutar
main()
