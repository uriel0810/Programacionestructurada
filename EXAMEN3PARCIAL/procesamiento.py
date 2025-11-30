import sys
import collections

sys.setrecursionlimit(4000)

class NodoSplit:
    """Nodo que divide la secuencia de entrada: impares a Salida 1, pares a Salida 2."""
    def __init__(self, id_nodo, salidas):
        self.id = id_nodo
        self.salidas = salidas  # {1: salida1, 2: salida2}

class NodoMerge:
    """Nodo que fusiona dos secuencias alternando E1,E2,E1,E2..."""
    def __init__(self, id_nodo, entradas):
        self.id = id_nodo
        self.entradas = entradas  # [entrada1, entrada2]

class SplitstreamNetwork:
    """Gestiona la red acíclica y calcula origen por memoización."""
    
    def __init__(self, m_global):
        self.nodes = {}
        self.m_global = m_global
        self.origen_map = {}

    def agregar_split(self, id_nodo, salidas):
        self.nodes[id_nodo] = NodoSplit(id_nodo, salidas)

    def agregar_merge(self, id_nodo, entradas):
        self.nodes[id_nodo] = NodoMerge(id_nodo, entradas)

    def calcular_origen_global(self, id_nodo, k):
        """
        Retorna la posición en la secuencia global que genera la posición k
        de la salida id_nodo.
        """
        if k <= 0:
            return None
        
        if id_nodo == 0:
            return k  # Estás leyendo directamente la secuencia global

        if (id_nodo, k) in self.origen_map:
            return self.origen_map[(id_nodo, k)]

        nodo = self.nodes.get(id_nodo, None)

        # Si el nodo no existe o está mal definido:
        if nodo is None:
            # No sabemos resolver → inválido
            return None

        resultado = None

        # -----------------------
        # CASO MERGE
        # -----------------------
        if isinstance(nodo, NodoMerge):

            if k % 2 == 1:
                # Índices impares vienen de entrada 1
                k_origen = (k + 1) // 2
                nodo_origen_id = nodo.entradas[0]
            else:
                # Índices pares vienen de entrada 2
                k_origen = k // 2
                nodo_origen_id = nodo.entradas[1]

            resultado = self.calcular_origen_global(nodo_origen_id, k_origen)

        # -----------------------
        # CASO SPLIT
        # -----------------------
        elif isinstance(nodo, NodoSplit):
            # En split, la posición k en cualquiera de sus salidas
            # proviene de la posición k en la entrada
            resultado = self.calcular_origen_global(0, k)

        # Guardar memoización
        self.origen_map[(id_nodo, k)] = resultado
        return resultado


def resolver_splitstream():
    """Función principal para lectura interactiva."""
    
    print("--- PROCESAMIENTO DE SECUENCIAS - SPLITSTREAM ---")
    
    try:
        m = int(input("Longitud de la secuencia global (m): "))
        n = int(input("Número de nodos (n): "))
        q = int(input("Número de consultas (q): "))

        if m <= 0 or n <= 0 or q <= 0:
            print("Valores deben ser positivos.")
            return

        network = SplitstreamNetwork(m)

        print("\nIngrese la descripción de los nodos:")
        print(" Split : S <id> <salida1> <salida2>")
        print(" Merge : M <id> <entrada1> <entrada2>")

        for _ in range(n):
            parts = input().split()
            if not parts:
                continue

            tipo = parts[0].upper()
            id_nodo = int(parts[1])

            if tipo == 'S':
                salida1, salida2 = map(int, parts[2:4])
                network.agregar_split(id_nodo, {1: salida1, 2: salida2})

            elif tipo == 'M':
                entrada1, entrada2 = map(int, parts[2:4])
                network.agregar_merge(id_nodo, [entrada1, entrada2])

        print("\nConsultas (salida_final, k):")
        resultados = []

        for i in range(q):
            try:
                parts = input(f"Consulta {i+1}: ").split()
                salida, k = map(int, parts)

                origen = network.calcular_origen_global(salida, k)

                if origen is None or origen > m:
                    resultados.append(f"({salida}, {k}) -> none")
                else:
                    resultados.append(f"({salida}, {k}) -> {origen}")

            except:
                resultados.append(f"Consulta {i+1}: error de formato")

        print("\n--- RESULTADOS ---")
        for r in resultados:
            print(r)

    except Exception as e:
        print("Error general:", e)


# EJECUCIÓN CORRECTA
if __name__ == "__main__":
    resolver_splitstream()
