#include <stdio.h>

int main() {
    float voltaje;

    printf("Ingrese el voltaje del circuito: ");
    scanf("%f", &voltaje);

    // Verificar si el voltaje está fuera del rango 220-240
    if (voltaje < 220 || voltaje > 240) {
        printf("Alarma activada: Voltaje fuera de rango.\n");
    } else {
        printf("Voltaje dentro del rango, sin alarma.\n");
    }

    return 0;
}
