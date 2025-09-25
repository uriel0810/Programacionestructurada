

corriente = float(input("Ingrese la corriente medida (A): "))
voltaje = float(input("Ingrese el voltaje medido (V): "))

# Condición compuesta
if corriente > 3 and voltaje < 1:
    print("Alarma de cortocircuito ACTIVADA.")
else:
    print("Sistema en monitoreo continuo...")
