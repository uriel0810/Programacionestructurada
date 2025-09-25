voltaje = float(input("Ingrese el voltaje de la bateria (V): "))

if voltaje < 11:
    print("Bateria baja.")
elif voltaje <= 12.6:
    print("Bateria normal.")
else:
    print("Sobrecarga.")
