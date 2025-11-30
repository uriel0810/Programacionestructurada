import sys

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def solve():
    line = sys.stdin.readline().strip()
    if not line:
        return
    dx_dy = list(map(int, line.split()))
    if len(dx_dy) != 2:
        print("IMPOSSIBLE")
        return
    dx, dy = dx_dy
    # lectura k
    try:
        k = int(sys.stdin.readline().strip())
    except:
        print("IMPOSSIBLE")
        return

    winds = []
    all_x = []
    all_y = []

    for _ in range(k):
        parts = sys.stdin.readline().strip().split()
        while len(parts) == 0:
            parts = sys.stdin.readline().strip().split()
        if len(parts) < 2:
            print("IMPOSSIBLE")
            return
        wx, wy = map(int, parts[:2])

        # número de límites para este viento
        line = sys.stdin.readline().strip()
        while line == "":
            line = sys.stdin.readline().strip()
        n = int(line)

        limits = []
        for _ in range(n):
            x,y = map(int, sys.stdin.readline().split())
            limits.append((x,y))
            all_x.append(x)
            all_y.append(y)
        winds.append((wx, wy, limits))

    # Determinar si las coordenadas vienen 1-based (1..dx) o 0-based (0..dx-1).
    use_one_based = False
    if len(all_x) > 0:
        min_x = min(all_x); max_x = max(all_x)
        min_y = min(all_y); max_y = max(all_y)
        # si no aparece 0 y todos están en 1..dx y 1..dy, asumimos 1-based
        if min_x >= 1 and max_x <= dx and min_y >= 1 and max_y <= dy and (0 not in all_x and 0 not in all_y):
            use_one_based = True

    # Grid for forced values: -1 = free, 0 = forced empty, 1 = forced molecule
    forced = [[-1] * dx for _ in range(dy)]

    # Aplico restricciones
    for wx, wy, limits in winds:
        for (xorig, yorig) in limits:
            x = xorig - 1 if use_one_based else xorig
            y = yorig - 1 if use_one_based else yorig

            # Si la posición límite (x,y) está fuera de la grilla -> no puede cumplirse
            if not (0 <= x < dx and 0 <= y < dy):
                print("IMPOSSIBLE")
                return

            # forzar (x,y) = 1
            if forced[y][x] == 0:
                print("IMPOSSIBLE")
                return
            forced[y][x] = 1

            # forzar (x+wx, y+wy) = 0 si está dentro de la grilla
            xx = x + wx
            yy = y + wy
            if 0 <= xx < dx and 0 <= yy < dy:
                if forced[yy][xx] == 1:
                    print("IMPOSSIBLE")
                    return
                forced[yy][xx] = 0

    # Construir solución mínima: solo '*' donde forced==1
    min_grid = [['.' for _ in range(dx)] for _ in range(dy)]
    for y in range(dy):
        for x in range(dx):
            if forced[y][x] == 1:
                min_grid[y][x] = '*'

    # Construir solución máxima: '*' en cualquier celda que NO esté forzada a 0
    max_grid = [['*' for _ in range(dx)] for _ in range(dy)]
    for y in range(dy):
        for x in range(dx):
            if forced[y][x] == 0:
                max_grid[y][x] = '.'
            # forced==1 sigue siendo '*', forced==-1 también '*'

    # Imprimir: primero mínima, luego una línea en blanco, luego máxima
    for row in min_grid:
        print(''.join(row))
    print()
    for row in max_grid:
        print(''.join(row))


if __name__ == "__main__":
    solve()