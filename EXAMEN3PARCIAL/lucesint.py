# -----------------------------------------------------
# Resolver sistema A x = b en GF(2) con solución mínima
# para togglear luces con interruptores.
# -----------------------------------------------------

def gauss_gf2(A, b):
    """
    Gauss-Jordan sobre GF(2).
    Devuelve:
    - rank
    - A transformada
    - b transformado
    - pos_pivote: variable pivote por fila
    """
    n = len(A)
    m = len(A[0])

    row = 0
    pos_pivote = [-1] * n

    for col in range(m):
        # buscar fila con 1 en esta columna
        sel = -1
        for r in range(row, n):
            if A[r][col] == 1:
                sel = r
                break
        
        if sel == -1:
            continue
        
        # intercambiar filas
        A[row], A[sel] = A[sel], A[row]
        b[row], b[sel] = b[sel], b[row]
        pos_pivote[row] = col

        # Eliminar en otras filas
        for r in range(n):
            if r != row and A[r][col] == 1:
                for c in range(col, m):
                    A[r][c] ^= A[row][c]
                b[r] ^= b[row]

        row += 1
        if row == n:
            break

    return row, A, b, pos_pivote



def solve_min_solution(A, b):
    """
    Resuelve A x = b (GF(2)) y devuelve la solución de menor peso.
    Si no hay solución → None.
    """
    n = len(A)
    m = len(A[0])

    rank, A2, b2, piv = gauss_gf2(A, b)

    # Verificar inconsistencia: 0 = 1
    for i in range(rank, n):
        if b2[i] == 1:
            return None

    # Variables libres
    free_vars = [j for j in range(m) if j not in piv]

    best_sol = None
    best_weight = 10**9

    # Probar todas las combinaciones de variables libres (usualmente pocas)
    import itertools

    for mask in itertools.product([0,1], repeat=len(free_vars)):
        x = [0] * m

        # poner libres
        for idx, val in zip(free_vars, mask):
            x[idx] = val

        # calcular pivotes
        for i in reversed(range(rank)):
            col = piv[i]
            s = b2[i]
            for j in range(col+1, m):
                s ^= (A2[i][j] & x[j])
            x[col] = s

        weight = sum(x)
        if weight < best_weight:
            best_weight = weight
            best_sol = x

    return best_sol



def main():
    # Leer entrada
    n, m = map(int, input().split())

    ini = list(map(int, input().split()))
    fin = list(map(int, input().split()))

    # b = fin XOR ini
    b = [(fin[i] ^ ini[i]) for i in range(n)]

    A = [[0]*m for _ in range(n)]

    for j in range(m):
        datos = list(map(int, input().split()))
        k = datos[0]
        luces = datos[1:]
        for luz in luces:
            A[luz-1][j] = 1

    # Resolver
    sol = solve_min_solution(A, b)

    if sol is None:
        print("impossible")
        return

    # Mostrar número mínimo
    print(sum(sol))

    # mostrar secuencia (1-based index)
    seq = [i+1 for i, x in enumerate(sol) if x == 1]
    if seq:
        print(*seq)
    else:
        print()  # sin activaciones


# -----------------------------------------------------
# Ejecutar
# -----------------------------------------------------
main()
