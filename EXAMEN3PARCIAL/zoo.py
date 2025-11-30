# -------------------------------------------------------
# Verificar si se puede transformar la distribución
# de animales en la deseada usando movimientos simultáneos.
# -------------------------------------------------------

from collections import defaultdict, deque

def main():
    # Leer n = recintos, m = túneles
    n, m = map(int, input().split())

    # Animales actuales y deseados
    actual = input().split()
    final = input().split()

    # Grafo de túneles
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    # Usar BFS para encontrar componentes conexas
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            # Obtener la componente
            comp = []
            queue = deque([i])
            visited[i] = True

            while queue:
                u = queue.popleft()
                comp.append(u)
                for v in g[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)

            # Revisar multiset de animales dentro de la componente
            count_actual = defaultdict(int)
            count_final = defaultdict(int)

            for node in comp:
                count_actual[actual[node]] += 1
                count_final[final[node]] += 1

            # Si difieren, no se puede reacomodar por simultaneidad
            if count_actual != count_final:
                print("impossible")
                return

    # Si todas las componentes tienen las mismas multisets:
    print("possible")


# Ejecutar
main()
