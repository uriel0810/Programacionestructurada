from fractions import Fraction
from itertools import combinations

# Preguntas fijas del sistema
PREGUNTAS = [
    (1, 1, 1),
    (2, 1, 0),
    (0, 2, 1),
    (3, 0, 1),
    (0, 1, 3)
]

def resolver_sistema_3x3(ec):
    """
    ec: lista de 3 ecuaciones (a, b, c, resultado)
    Usa eliminación Gaussiana con Fraction (aritmética exacta).
    Devuelve (x, y, z) enteros si existe solución válida, o None.
    """
    # Construir matriz aumentada
    M = []
    for a, b, c, r in ec:
        M.append([Fraction(a), Fraction(b), Fraction(c), Fraction(r)])

    # Eliminación Gaussiana
    for col in range(3):
        # Encontrar renglón pivote
        pivot = None
        for row in range(col, 3):
            if M[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            return None  # sistema sin solución única

        # Intercambiar si es necesario
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]

        # Normalizar fila pivote
        factor = M[col][col]
        M[col] = [v / factor for v in M[col]]

        # Eliminar en las otras filas
        for row in range(3):
            if row != col and M[row][col] != 0:
                factor = M[row][col]
                M[row] = [
                    M[row][i] - factor * M[col][i]
                    for i in range(4)
                ]

    # Solución final
    x, y, z = M[0][3], M[1][3], M[2][3]

    # Deben ser enteros
    if x.denominator == 1 and y.denominator == 1 and z.denominator == 1:
        x, y, z = int(x), int(y), int(z)
        if x >= 0 and y >= 0 and z >= 0:
            return (x, y, z)

    return None


def verificar(sol, preguntas, respuestas):
    """Cuenta cuántas ecuaciones NO se cumplen."""
    x, y, z = sol
    fallos = 0
    for (a, b, c), r in zip(preguntas, respuestas):
        if a*x + b*y + c*z != r:
            fallos += 1
    return fallos


def resolver_con_mentira(preguntas, respuestas):
    """Prueba todas las combinaciones para detectar la mentira."""
    soluciones = set()

    # la mentira puede estar en cualquier ecuación
    for mentira in range(5):
        restantes = [i for i in range(5) if i != mentira]

        # tomar combinaciones de 3 ecuaciones correctas
        for trio in combinations(restantes, 3):
            ec = []
            for idx in trio:
                a, b, c = preguntas[idx]
                r = respuestas[idx]
                ec.append((a, b, c, r))

            sol = resolver_sistema_3x3(ec)
            if sol is None:
                continue

            # verificar que solo exista una mentira
            if verificar(sol, preguntas, respuestas) == 1:
                soluciones.add(sol)

    return list(soluciones)


def main():
    print("=== ACERTIJO DE LA ESFINGE ===\n")
    respuestas = []

    for i, (a, b, c) in enumerate(PREGUNTAS, start=1):
        r = int(input(f"Pregunta {i}: ¿Patas totales de {a} axex, {b} basiliso, {c} centauro? "))
        respuestas.append(r)

    sols = resolver_con_mentira(PREGUNTAS, respuestas)

    if len(sols) == 1:
        x, y, z = sols[0]
        print("\nSOLUCIÓN ENCONTRADA:")
        print(f"Axex = {x}")
        print(f"Basiliso = {y}")
        print(f"Centauro = {z}")
    elif len(sols) == 0:
        print("\nNo se pudo encontrar solución válida.")
    else:
        print("\nHay varias soluciones posibles:")
        for sol in sols:
            print(sol)


if __name__ == "__main__":
    main()
