import collections
import sys

# Ajuste para evitar errores de límite de recursión en árboles grandes.
sys.setrecursionlimit(2000)

# --- Clase para la Mazmorra (Grafo/Árbol con Pesos) ---
class Dungeon:
    """Representa la mazmorra como un árbol de salas y pasillos con tiempos."""
    def __init__(self, n_salas):
        self.n = n_salas
        self.adj = collections.defaultdict(list)
        self.total_time_sum = 0  # Suma de todos los tiempos de pasillo (S)

    def agregar_pasillo(self, u, v, tiempo):
        """Añade una conexión bidireccional entre dos salas."""
        if u < 1 or u > self.n or v < 1 or v > self.n or tiempo <= 0:
            raise ValueError("Pasillo inválido: nodos fuera de rango (1 a N) o tiempo no positivo.")

        self.adj[u].append((v, tiempo))
        self.adj[v].append((u, tiempo))
        self.total_time_sum += tiempo

    def bfs_distancia(self, inicio):
        """Calcula el tiempo mínimo desde 'inicio' a todas las demás salas."""
        distancias = {i: float('inf') for i in range(1, self.n + 1)}

        cola = collections.deque([(inicio, 0)])
        distancias[inicio] = 0

        while cola:
            u, d = cola.popleft()

            for v, t in self.adj[u]:
                if distancias[v] == float('inf'):
                    distancias[v] = d + t
                    cola.append((v, d + t))

        return distancias


def resolver_escenario(dungeon, inicio, llave, trampa):
    """Calcula el tiempo mínimo para explorar todas las salas con restricciones."""

    if not (1 <= inicio <= dungeon.n and 1 <= llave <= dungeon.n and 1 <= trampa <= dungeon.n):
        return "IMPOSSIBLE"

    # Distancia mínima desde inicio a trampa
    dist_i = dungeon.bfs_distancia(inicio)
    t_i_t = dist_i.get(trampa, float('inf'))

    if t_i_t == float('inf'):
        return "IMPOSSIBLE"

    # Fórmula general de recorrido mínimo en árbol
    tiempo_minimo = 2 * dungeon.total_time_sum - t_i_t

    return int(tiempo_minimo)


def dungeon_crawler_main():
    """Función principal."""
    try:
        print("--- Explorador de Mazmorras (Dungeon Crawler) ---")
        print("Ingrese n (salas) y q (consultas) separados por espacio (e.g., 5 2):")

        line = sys.stdin.readline().strip()
        if not line:
            return

        parts = line.split()
        if len(parts) != 2:
            print("Error: n y q deben ser 2 números enteros.")
            return

        n, q = map(int, parts)

        if n < 1:
            print("Error: n debe ser positivo.")
            return

        dungeon = Dungeon(n)

        if n > 1:
            print(f"\nIngrese {n - 1} pasillos en formato: u v tiempo:")
            for i in range(n - 1):
                line = sys.stdin.readline().strip()
                if not line:
                    print(f"Advertencia: Se esperaban {n-1} pasillos.")
                    break

                parts = line.split()
                if len(parts) != 3:
                    print(f"Error en pasillo {i+1}. Se esperaban 3 enteros.")
                    return

                u, v, t = map(int, parts)
                dungeon.agregar_pasillo(u, v, t)

        print(f"\nTotal de tiempo de aristas (S): {dungeon.total_time_sum}")

        print(f"\nIngrese {q} escenarios en formato: inicio llave trampa:")

        resultados = []
        for i in range(q):
            print(f"Escenario {i+1}:", end=" ")
            line = sys.stdin.readline().strip()
            if not line:
                break

            parts = line.split()
            if len(parts) != 3:
                resultados.append(f"Escenario {i+1}: IMPOSSIBLE (Formato incorrecto)")
                continue

            inicio, llave, trampa = map(int, parts)

            if n == 1:
                tiempo = 0 if inicio == llave == trampa == 1 else "IMPOSSIBLE"
            else:
                tiempo = resolver_escenario(dungeon, inicio, llave, trampa)

            resultados.append(
                f"Escenario {i+1} (I:{inicio}, L:{llave}, T:{trampa}): {tiempo}"
            )

        print("\n--- RESULTADOS FINALES ---")
        for r in resultados:
            print(r)

    except Exception as e:
        print(f"Error general: {e}")


if __name__ == "__main__":
    dungeon_crawler_main()
