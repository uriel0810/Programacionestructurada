# Programa para activar alarma según voltaje

voltaje = float(input("Ingrese el voltaje del circuito: "))

# Verificar si está fuera del rango
if voltaje < 220 or voltaje > 240:
    print(" Alarma activada: Voltaje fuera de rango.")
else:
    print(" Voltaje dentro del rango, sin alarma.")
