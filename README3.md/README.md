##1. Descripción del problema
Un grupo de amigos planea un viaje y necesita dividir los gastos de gasolina, comida y hospedaje entre los participantes.
 El programa debe solicitar:
Cantidad de personas.


Monto de cada gasto (gasolina, comida, hospedaje).


Posteriormente, calculará el total y determinará cuánto debe pagar cada uno. Además, se deben aplicar condiciones especiales:
Si algún participante consume más comida, su monto será mayor.


Si alguien se hospeda en habitación privada, también pagará un extra.


El objetivo es lograr una distribución justa, eficiente y transparente de los gastos.

2. Relevancia del uso de conceptos de programación
Variables: permiten organizar los datos ingresados por el usuario (gastos, número de personas, condiciones especiales).


Operadores aritméticos: posibilitan calcular totales, promedios y ajustes individuales.


Sentencias selectivas (if/else): ayudan a manejar las excepciones (más consumo de comida o habitación privada), garantizando equidad en el reparto.


3. Proceso de desarrollo
a) Análisis
Se identificaron las entradas, procesos y salidas:
Entradas: número de personas, gasto en gasolina, gasto en comida, gasto en hospedaje, condiciones especiales.


Proceso: sumar los gastos, dividir entre los participantes, ajustar los pagos según las condiciones.


Salida: cuánto paga cada persona.


b) Diseño en DFD (Diagrama de Flujo de Datos)
Inicio


Ingreso de datos (personas y gastos).


Cálculo del gasto total.


División del gasto entre las personas.


Aplicación de condiciones especiales.


Mostrar resultados.


Fin


c) Implementación en código
Se implementó en lenguaje C utilizando:
scanf para capturar datos.


Operadores + y / para cálculos.


Sentencias if/else para las condiciones especiales.
implementacion de loop con el comando for i 


4. Dificultades encontradas y soluciones
Problema: manejar excepciones individuales sin usar bucles.


Solución: aplicar condiciones if/else para cada participante de forma explícita.


Problema: dividir los gastos de forma justa cuando alguien consume más.


Solución: sumar recargos fijos al monto base correspondiente a esa persona.
