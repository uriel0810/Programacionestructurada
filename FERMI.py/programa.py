import math

# Constantes
k = 8.617333262e-5  # eV/K
T = 300
kT = k * T

# Propiedades de materiales
materiales = {
    "Si": {
        "Eg": 1.12,
        "Nc": 2.8e19,
        "Nv": 1.04e19,
    },
    "GaAs": {
        "Eg": 1.42,
        "Nc": 4.7e17,
        "Nv": 7.0e18,
    }
}

print("=== CÁLCULO INTERACTIVO DEL NIVEL DE FERMI ===\n")
print("Materiales disponibles: Si, GaAs")
mat = input("Selecciona el material: ").strip()

if mat not in materiales:
    print("Material no válido.")
    exit()

tipo = input("Tipo de semiconductor (n / p): ").strip().lower()
dopado = float(input("Ingresa la concentración de dopado (cm^-3): "))

Eg = materiales[mat]["Eg"]
Nc = materiales[mat]["Nc"]
Nv = materiales[mat]["Nv"]

Ev = 0
Ec = Eg

if tipo == "n":
    EF = Ec - kT * math.log(Nc / dopado)
elif tipo == "p":
    EF = Ev + kT * math.log(Nv / dopado)
else:
    print("Tipo inválido.")
    exit()

print("\n===== RESULTADOS =====")
print(f"Material: {mat}")
print(f"Tipo: {tipo}")
print(f"Dopado = {dopado:.3e} cm^-3")
print(f"Nivel de Fermi EF = {EF:.5f} eV (referido a Ev = 0)")
print(f"Ec = {Ec} eV")
print("======================")