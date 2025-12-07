import numpy as np
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
    Ev = 0
    kT = kB_eV * T

    # evitar overflow
    n = Nc * math.exp(max(-(Ec - Ef) / kT, -700))
    p = Nv * math.exp(max(-(Ef - Ev) / kT, -700))
    return n, p

def neutrality(Ef, ND, NA, mat, T):
    n, p = n_p_of_Ef(Ef, mat, T)
    return n - p - (ND - NA)

def solve_Ef(ND, NA, mat, T):
    # rango amplio
    a, b = -5, mat["Eg"] + 5
    fa = neutrality(a, ND, NA, mat, T)
    fb = neutrality(b, ND, NA, mat, T)

    # si no hay cambio de signo, devolver midgap
    if fa * fb > 0:
        return mat["Eg"] / 2

    # bisección
    for _ in range(200):
        m = 0.5 * (a + b)
        fm = neutrality(m, ND, NA, mat, T)
        if abs(fm) < 1e-9:
            return m
        if fa * fm < 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    return m

def main():
    T = 300
    doping = np.logspace(10, 18, 20)  # menos puntos para impresión

    print("\n=== NIVELES DE FERMI PARA Si Y GaAs (tipo-n) ===\n")
    
    for mat_name in ["Si", "GaAs"]:
        print(f"\nMaterial: {mat_name}")
        mat = materials[mat_name]
        print("Dopado (cm^-3)     EF (eV)")
        for ND in doping:
            Ef = solve_Ef(ND, 0, mat, T)
            print(f"{ND:12.3e}   {Ef: .4f}")

    # ejemplo GaAs ND=1e16
    ND_ex = 1e16
    mat = materials["GaAs"]
    Ef = solve_Ef(ND_ex, 0, mat, T)
    n, p = n_p_of_Ef(Ef, mat, T)
    ni = math.sqrt(mat["Nc"] * mat["Nv"]) * math.exp(-mat["Eg"] / (2 * kB_eV * T))

    print("\n=== EJEMPLO GaAs ND = 1e16 cm^-3 ===")
    print(f"EF  = {Ef:.5f} eV")
    print(f"n   = {n:.3e} cm^-3")
    print(f"p   = {p:.3e} cm^-3")
    print(f"ni  = {ni:.3e} cm^-3\n")

main()