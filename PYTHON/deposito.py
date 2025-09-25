nivel = float(input("Ingrese el nivel del deposito (en %): "))

if nivel < 10:
    print("Deposito vacio.")
elif nivel <= 90:
    print("Niveles normales.")
else:
    print("Posible desbordamiento.")

