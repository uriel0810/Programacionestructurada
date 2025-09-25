
# Programa para controlar la lámpara según la lectura de luz

# Solicitar la lectura del sensor
lux = int(input("Ingrese la lectura del sensor de luz (en lux): "))

# Condición con if-else
if lux < 300:
    print("La lámpara debe ENCENDERSE.")
else:
    print("La lámpara debe APAGARSE.")
