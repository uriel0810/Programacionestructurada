# Programa para clasificar la temperatura

temperatura = float(input("Ingrese la temperatura en °C: "))

if temperatura < 50:
    print("Frío")
elif 50 <= temperatura <= 150:
    print("Temperatura Normal")
else:
    print("Alerta: Caliente")
