frecuencia = float(input("Ingrese la frecuencia (Hz): "))

if frecuencia < 20:
    print("Sub-sonido.")
elif frecuencia <= 20000:
    print("Sonido.")
else:
    print("Ultrasonido.")

