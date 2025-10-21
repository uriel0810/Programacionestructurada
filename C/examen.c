#include <stdio.h>

int main() {
    int personas, i;
    float gasolina, comida, hospedaje, total, base, pagoExtra, pagoFinal;

    printf("Ingrese la cantidad de personas: ");
    scanf("%d", &personas);

    printf("Ingrese el gasto de gasolina: ");
    scanf("%f", &gasolina);

    printf("Ingrese el gasto de comida: ");
    scanf("%f", &comida);

    printf("Ingrese el gasto de hospedaje: ");
    scanf("%f", &hospedaje);

    total = gasolina + comida + hospedaje;
    base = total / personas;

    printf("\nGasto total del viaje: %.2f\n", total);
    printf("Pago base por persona: %.2f\n\n", base);

    for (i = 1; i <= personas; i++) {
        int extraComida, privado;
        pagoExtra = 0;

        printf("Persona %d:\n", i);

        printf("  ¿Consumio mas comida? (1=Si, 0=No): ");
        scanf("%d", &extraComida);
        if (extraComida == 1) {
            pagoExtra += comida * 0.1;  // 10% extra de comida
        }

        printf("  ¿Se hospedo en habitacion privada? (1=Si, 0=No): ");
        scanf("%d", &privado);
        if (privado == 1) {
            pagoExtra += hospedaje * 0.2; // 20% extra de hospedaje
        }

        pagoFinal = base + pagoExtra;
        printf("  Total a pagar: %.2f\n\n", pagoFinal);
    }

    return 0;
}
