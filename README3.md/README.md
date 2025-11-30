1. Programas basados en grafos y árboles

Varios problemas se resolvieron usando grafos, ya sea para representar conexiones entre salas, túneles, botones, luces o estructuras físicas.

Metodología utilizada

Convertir cada sistema (túneles, pasillos, conexiones) en un grafo.

Aplicar BFS o DFS para identificar componentes conectadas.

Cuando era necesario, usar propiedades especiales como:

Árboles → recorrer caminos mínimos y subárboles.

Componentes → verificar si ciertas transformaciones eran posibles dentro de cada parte del grafo.

Resultado

Esto permitió resolver problemas como el de los recintos del zoológico, las salas con llave y trampa, y el mosaico en 2D, aplicando lógica de recorridos y validaciones de conectividad.

2. Programas con álgebra lineal y operaciones en GF(2) o GF(3)

Algunos ejercicios requerían modelar cambios de estado mediante sistemas de ecuaciones modulares, especialmente cuando:

Las luces cambiaban con interruptores (XOR → GF(2))

Los colores cambiaban con ciclos de 3 estados (GF(3))

Los botones afectaban subconjuntos de luces.

Metodología utilizada

Representar cada interruptor/botón como una columna en una matriz.

Representar cada luz como una fila.

Modelar el problema como:

A * x = b   sobre un cuerpo finito (mod 2 o mod 3)


Resolver el sistema mediante:

Eliminación Gaussiana sobre GF(2) o GF(3).

Identificar variables libres.

Seleccionar la solución de menor peso (minimizando interruptores presionados).

Resultado

Este enfoque permitió obtener:

La solución mínima en el problema de interruptores.

La validación de imposibilidad cuando no existía solución.

Modelos matemáticos correctos y eficientes.

3. Búsqueda de patrones en matrices (motivo y mosaico)

Para el problema del mosaico se trataba de ubicar un patrón 2D dentro de una matriz mayor.

Metodología

Implementar una búsqueda tipo fuerza bruta optimizada.

Recorrer todas las posiciones posibles del mosaico donde el patrón puede caber.

Verificar celda por celda:

Si el motivo tiene color → comparación estricta.

Si el motivo tiene 0 → cualquier color es válido.

Resultado

El programa identifica todas las coincidencias y las reporta de forma ordenada.

4. Simulación y redes de procesamiento (Splitstream)

En el sistema Split/Merge se debían rastrear elementos sin simular toda la secuencia.

Metodología

Analizar matemáticamente cómo se distribuyen los índices:

Split: índices impares a una salida, pares a otra.

Merge: alterna entre dos entradas.

Seguir el índice hacia atrás para determinar de dónde proviene un elemento.

Implementar funciones recursivas o directas para calcular la posición K sin generar toda la secuencia.

Resultado

Las consultas se resolvieron eficientemente sin construir toda la red.

5. Sistemas con restricciones físicas (mazmorra, zoológico, vientos)

En estos problemas se exigía modelar condiciones más realistas:

Mazmorra

Se utilizó la estructura de árbol y rutas para asegurar:

No visitar la trampa antes que la llave.

Recorridos mínimos usando distancias acumuladas.

Zoológico

Se verificó que el reacomodo fuera posible si:

En cada componente conectada existe la misma cantidad de cada animal al inicio y al final.

Esto se basó en las propiedades de permutaciones dentro de grafos.

Cristal y vientos

Para los límites de moléculas, se generaron configuraciones mínima y máxima respetando:

Que si hay molécula en (x, y) y viento (wx, wy), entonces no puede haber en (x+wx, y+wy) en la configuración mínima.

En la máxima, se permiten más moléculas pero siempre respetando restricciones.

Resultado

Los modelos respetan tanto la lógica formal como la física simulada en cada problema.

Conclusión General

Los programas desarrollados aplican distintos enfoques según la naturaleza del problema:

Grafos para conexiones físicas y movimientos.

Álgebra lineal modular para cambios de estado (luces, botones, colores).

Matching 2D para búsquedas en rejillas.

Rutas óptimas en árboles.

Simulación matemática para redes de procesamiento.

Todos los algoritmos fueron diseñados para ser:

Correctos en términos lógicos.

Eficientes dentro de lo requerido.

Claros y mantenibles, como lo haría un estudiante con base en los conceptos aprendidos.
