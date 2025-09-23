import math

def densidad_electrones_libres():
    # Constante de Boltzmann en eV/K
    k = 8.617e-5  

    # Constantes C de cada material (en cm^-3 K^-3/2)
    materiales = {
        "Ge": {"Eg": 0.66, "C": 1.66e15},
        "Si": {"Eg": 1.12, "C": 5.29e15},
        "GaAs": {"Eg": 1.42, "C": 2.10e18}
    }

    # Entrada del usuario
    material = input("Ingrese el material (Si/Ge/GaAs): ").strip()
    T = float(input("Ingrese la temperatura en Kelvin: "))

    if material not in materiales:
        print("Material no disponible en la base de datos.")
        return

    # Parámetros del material
    Eg = materiales[material]["Eg"]
    C = materiales[material]["C"]

    # Fórmula: ni = C * T^(3/2) * exp(-Eg / (2*k*T))
    ni = C * (T ** 1.5) * math.exp(-Eg / (2 * k * T))

    print(f"\nLa densidad intrínseca de electrones en {material} a {T} K es: {ni:.3e} cm^-3")

# Ejecutar la función
densidad_electrones_libres()
