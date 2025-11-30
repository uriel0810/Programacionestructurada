#include <stdio.h>

#define JUG 4      // jugadores
#define CARTAS 32  // 8 conjuntos × 4 cartas

// Dueño de cada carta (0 = desconocido, 1-4 = jugador actual, -1 = retirada en cuarteto)
int dueño[CARTAS + 1] = {0};

// Saber a qué conjunto pertenece una carta (1_8)
int conjunto(int carta) {
    return (carta - 1) / 4 + 1;
}

// Saber cuál es la primera carta de ese conjunto
int baseConjunto(int cto) {
    return (cto - 1) * 4 + 1;
}

int main() {
    int n;
    scanf("%d", &n);

    for (int accion = 1; accion <= n; accion++) {
        char tipo[10];
        int A, B, carta;
        scanf("%s", tipo);

        if (tipo[0] == 'A') {  
            // ASK A B carta
            scanf("%d %d %d", &A, &B, &carta);

            int cto = conjunto(carta);
            int tiene = 0;

            // Verificar si el jugador A tiene al menos una carta del conjunto
            int inicio = baseConjunto(cto);
            for (int x = inicio; x < inicio + 4; x++) {
                if (dueño[x] == A)
                    tiene = 1;
            }

            if (!tiene) {
                printf("no %d\n", accion);
                return 0;
            }

        } else if (tipo[0] == 'G') {
            // GIVE B A carta
            scanf("%d %d %d", &B, &A, &carta);

            // Si ya sabemos quién la tenía, debe coincidir
            if (dueño[carta] != 0 && dueño[carta] != B) {
                printf("no %d\n", accion);
                return 0;
            }

            dueño[carta] = A;

        } else if (tipo[0] == 'F') {
            // FAIL B A carta  (B niega tenerla)
            scanf("%d %d %d", &B, &A, &carta);

            // Si el estado dice que sí la tiene  trampa
            if (dueño[carta] == B) {
                printf("no %d\n", accion);
                return 0;
            }

        } else if (tipo[0] == 'R') {
            // RETIRA A cto
            scanf("%d %d", &A, &carta);
            int cto = carta;

            int inicio = baseConjunto(cto);

            // Las 4 cartas deben pertenecer a A
            for (int x = inicio; x < inicio + 4; x++) {
                if (dueño[x] != A && dueño[x] != 0) {
                    printf("no %d\n", accion);
                    return 0;
                }
                dueño[x] = -1; // cuarteto retirado
            }
        }
    }

    printf("yes\n");
    return 0;
}
