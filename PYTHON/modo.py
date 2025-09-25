modo = input("Ingrese el modo (A-automatico, M-manual, S-seguro): ")

if modo.upper() == 'A':
    print("Modo automatico activado.")
elif modo.upper() == 'M':
    print("Modo manual activado.")
elif modo.upper() == 'S':
    print("Modo seguro activado.")
else:
    print("Error: Modo invalido.")
