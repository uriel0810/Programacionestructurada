def score(A, B):
    """Probabilidad de que A gane a B: P(a > b)."""
    wins = 0
    total = len(A) * len(B)
    for a in A:
        for b in B:
            if a > b:
                wins += 1
    return wins / total

def main():
    # Leer D1
    data1 = list(map(int, input().split()))
    n1 = data1[0]
    D1 = data1[1:]

    # Leer D2
    data2 = list(map(int, input().split()))
    n2 = data2[0]
    D2 = data2[1:]

    # Tamaño del dado D3
    m = max(n1, n2)

    # Construimos D3 más débil posible y más fuerte posible
    minn = min(min(D1), min(D2))
    maxx = max(max(D1), max(D2))

    D3_min = [minn] * m      # Para minimizar P(D3 > D2)
    D3_max = [maxx] * m      # Para maximizar P(D3 > D1)

    p_min_D3_vs_D2 = score(D3_min, D2)
    p_max_D3_vs_D1 = score(D3_max, D1)

    print(f"{p_min_D3_vs_D2:.9f} {p_max_D3_vs_D1:.9f}")

if __name__ == "__main__":
    main()
