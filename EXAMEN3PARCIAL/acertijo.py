from fractions import Fraction
import itertools

#  RESOLVER SISTEMA 3x3 EXACTO

def solve_3x3(A, B):
    M = [[Fraction(A[i][j]) for j in range(3)] + [Fraction(B[i])] for i in range(3)]

    for col in range(3):
        pivot = None
        for r in range(col, 3):
            if M[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            return None

        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]

        p = M[col][col]
        M[col] = [v / p for v in M[col]]

        for r in range(3):
            if r != col:
                factor = M[r][col]
                M[r] = [M[r][c] - factor * M[col][c] for c in range(4)]

    return M[0][3], M[1][3], M[2][3]


#  DETECTAR LA RESPUESTA FALSA

def solve_with_one_lie(questions, answers):

    for lie in range(5):

        eqs = []
        vals = []

        for i in range(5):
            if i != lie:
                eqs.append(questions[i])
                vals.append(Fraction(answers[i]))

        for combo in itertools.combinations(range(4), 3):
            A = [eqs[i] for i in combo]
            B = [vals[i] for i in combo]

            sol = solve_3x3(A, B)
            if sol is None:
                continue

            x, y, z = sol

            if x < 0 or y < 0 or z < 0:
                continue
            if x != int(x) or y != int(y) or z != int(z):
                continue

            xi, yi, zi = int(x), int(y), int(z)

            ok = True
            for i in range(5):
                if i == lie:
                    continue
                a, b, c = questions[i]
                if a * xi + b * yi + c * zi != answers[i]:
                    ok = False
                    break

            if ok:
                return xi, yi, zi, lie

    return None



questions = []
answers = []

print("Ingresa 5 preguntas del tipo: a b c (enteros entre 0 y 10)")
for i in range(5):
    a, b, c = map(int, input(f"Pregunta {i+1} (a b c): ").split())
    questions.append((a, b, c))

print("\nIngresa ahora las respuestas de la Esfinge:")
for i in range(5):
    r = int(input(f"Respuesta {i+1}: "))
    answers.append(r)

sol = solve_with_one_lie(questions, answers)

print("\n======================")
if sol is None:
    print("No se pudo determinar una solución consistente con una sola mentira.")
else:
    axex, basiliso, centauro, lie_index = sol
    print(f"Axex = {axex} patas")
    print(f"Basiliso = {basiliso} patas")
    print(f"Centauro = {centauro} patas")
    print(f"La mentira está en la pregunta #{lie_index + 1}")