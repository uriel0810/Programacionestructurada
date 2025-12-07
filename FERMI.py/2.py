import math

kB_eV = 8.617333262145e-5  # eV/K

materials = {
    "Si":  {"Eg": 1.12, "Nc": 2.8e19, "Nv": 1.04e19},
    "GaAs":{"Eg": 1.42, "Nc": 4.7e17, "Nv": 7.0e18}
}

def n_p_of_Ef(Ef, mat, T):
    Nc = mat["Nc"]
    Nv = mat["Nv"]
    Eg = mat["Eg"]
    Ec = Eg
    Ev = 0.0
    kT = kB_eV * T

    n = Nc * math.exp(max(-(Ec - Ef) / kT, -700))
    p = Nv * math.exp(max(-(Ef - Ev) / kT, -700))
    return n, p

def neutrality(Ef, ND, NA, mat, T):
    n, p = n_p_of_Ef(Ef, mat, T)
    return n - p - (ND - NA)

def solve_Ef(ND, NA, mat, T):
    # Intervalo amplio donde seguramente está el EF
    a, b = -5, mat["Eg"] + 5
    fa = neutrality(a, ND, NA, mat, T)
    fb = neutrality(b, ND, NA, mat, T)

    # Si no hay cambio de signo, EF queda en el medio de la banda prohibida
    if fa * fb > 0:
        return mat["Eg"] / 2.0

    # Bisección clásica
    for _ in range(200):
        m = 0.5 * (a + b)
        fm = neutrality(m, ND, NA, mat, T)
        if abs(fm) < 1e-9:
            return m
        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm
    return m

def main():
    print("\n=== CÁLCULO INTERACTIVO DEL NIVEL DE FERMI ===\n")
    print("Materiales disponibles: Si, GaAs")
    material = input("Ingresa el material: ").strip()

    if material not in materials:
        print("Material no válido.")
        return
    
    tipo = input("Tipo de semiconductor (n / p): ").strip().lower()
    if tipo not in ["n", "p"]:
        print("Tipo no válido.")
        return
    
    try:
        dop = float(input("Ingresa la concentración de dopado (cm^-3): "))
    except:
        print("Valor inválido.")
        return

    T = 300  # temperatura fija

    mat = materials[material]
    if tipo == "n":
        ND, NA = dop, 0
    else:
        ND, NA = 0, dop

    Ef = solve_Ef(ND, NA, mat, T)
    n, p = n_p_of_Ef(Ef, mat, T)
    ni = math.sqrt(mat["Nc"] * mat["Nv"]) * math.exp(-mat["Eg"] / (2 * kB_eV * T))

    print("\n=== RESULTADOS ===")
    print(f"Material:       {material}")
    print(f"Tipo:           {tipo}")
    print(f"Dopado:         {dop:.3e} cm^-3")
    print(f"Temperatura:    {T} K")
    print(f"\nNivel de Fermi EF = {Ef:.6f} eV (Ev = 0)")
    print(f"n   = {n:.3e} cm^-3")
    print(f"p   = {p:.3e} cm^-3")
    print(f"ni  = {ni:.3e} cm^-3")
    print("==============================\n")

main()
