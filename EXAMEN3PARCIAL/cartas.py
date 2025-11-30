

def detectar_trampa(acciones):
    # Estado posible de cada carta:
    # dueño[carta] = {posibles dueños}
    # Cada carta inicia pudiendo pertenecer a cualquier jugador
    duenos_posibles = { (s, c): {0, 1, 2, 3} for s in range(8) for c in range(4) }

    # Registro de sets retirados
    retirado = [False]*8

    def contradiccion():
        # Si alguna carta no puede pertenecer a ningún jugador → imposible
        for card, posibles in duenos_posibles.items():
            if len(posibles) == 0:
                return True
        return False

    for i, ac in enumerate(acciones, start=1):

        tipo = ac[0]

        
        if tipo == "ask":
            A, B, s, c = ac[1:]

            # Regla: A no puede pedir si ES IMPOSIBLE que A tenga al menos una carta del set
            alguna_posible = False
            for x in range(4):
                if A in duenos_posibles[(s, x)]:
                    alguna_posible = True

            if not alguna_posible:
                return f"no {i}"

      
        elif tipo == "give":
            A, B, s, c = ac[1:]

            # Carta debe ser de A ahora
            duenos_posibles[(s, c)] = {A}

      
        elif tipo == "deny":
            A, B, s, c = ac[1:]

            # B afirma NO tener la carta → eliminarlo de posibles dueños
            if B in duenos_posibles[(s, c)]:
                duenos_posibles[(s, c)].remove(B)

        # ----------------------------------------
        # QUARTET: ("quartet", A, set_id)
        # ----------------------------------------
        elif tipo == "quartet":
            A, s = ac[1:]
            retirado[s] = True

            # Las cuatro cartas del set deben haber sido del jugador A
            for c in range(4):
                duenos_posibles[(s, c)] = {A}

        # Tras cada acción, verificar contradicciones
        if contradiccion():
            return f"no {i}"

    return "yes"


# -----------------------------------------------------------
# Ejemplo de uso
# -----------------------------------------------------------
if __name__ == "__main__":
    acciones = [
        ("ask", 0, 1, 2, 1),
        ("deny", 0, 1, 2, 1),
        ("ask", 1, 2, 2, 3),
        ("give", 2, 1, 2, 3),
        ("quartet", 1, 2)
    ]

    print(detectar_trampa(acciones))
