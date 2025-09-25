# Programa para controlar la velocidad del ventilador según la temperatura

temperatura = float(input("Ingrese la temperatura en °C: "))

if temperatura < 20:
    print("El ventilador está APAGADO.")
elif 20 <= temperatura <= 30:
    print("El ventilador está en BAJA VELOCIDAD.")
else:
    print("El ventilador está en ALTA VELOCIDAD.")
