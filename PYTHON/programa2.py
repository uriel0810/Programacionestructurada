import math

def densidad_electrones_libres():
    # Constante de Boltzmann en eV/K
    k = 8.617e-5  

    # Datos de materiales (Eg [eV], Nc [cm^-3], Nv [cm^-3])
    materiales = {
        "Si": {"Eg": 1.12, "Nc": 2.8e19, "Nv": 1.04e19},
        "Ge": {"Eg": 0.66, "Nc": 1.02e19, "Nv": 6.0e18},
        "GaAs": {"Eg": 1.42, "Nc": 4.7e17, "Nv": 7.0e18}
    }

    # Entrada del usuario
    material = input("Ingrese el material (Si/Ge/GaAs): ").strip()
    T = float(input("Ingrese la temperatura en Kelvin: "))

    if material not in materiales:
        print("Material no disponible en la base de datos.")
        return

    # Obtención de parámetros
    Eg = materiales[material]["Eg"]
    Nc = materiales[material]["Nc"]
    Nv = materiales[material]["Nv"]

    # Cálculo de densidad intrínseca de electrones (electrones/cm^3)
    ni = math.sqrt(Nc * Nv) * math.exp(-Eg / (2 * k * T))

    print(f"\nLa densidad de electrones libres (N1) en {material} a {T} K es: {ni:.3e} electrones/cm^3")

# Ejecutar función
densidad_electrones_libres()
