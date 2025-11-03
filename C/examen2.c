#include <stdio.h>

int main() {
    float km[7] = {10, 12, 20, 25, 11, 14, 8};
    float gasolina_total = 25.0;   // litros disponibles en la semana
    float consumo[7];              // consumo diario estimado
    float total_km = 0;
    int i, j;
    float temp;

    // Calcular el total de km recorridos en la semana
    for(i = 0; i < 7; i++) {
        total_km += km[i];
    }

    // Calcular los litros consumidos por día (proporcionalmente)
    for(i = 0; i < 7; i++) {
        consumo[i] = (km[i] / total_km) * gasolina_total;
    }

    printf("Consumo de gasolina diario (litros):\n");
    for(i = 0; i < 7; i++) {
        printf("Dia %d: %.2f L\n", i + 1, consumo[i]);
    }

    // Ordenar los consumos con Bubble Sort
    for(i = 0; i < 7 - 1; i++) {
        for(j = 0; j < 7 - i - 1; j++) {
            if(consumo[j] > consumo[j + 1]) {
                temp = consumo[j];
                consumo[j] = consumo[j + 1];
                consumo[j + 1] = temp;
            }
        }
    }

    printf("\nConsumo ordenado (de menor a mayor):\n");
    for(i = 0; i < 7; i++) {
        printf("%.2f L ", consumo[i]);
    }

    // Verificar si algún día requiere afinación
    printf("\n\nVerificacion de afinacion:\n");
    for(i = 0; i < 7; i++) {
        if(consumo[i] >= 12) {
            printf("Dia %d: %.2f L -> Ocupa afinacion.\n", i + 1, consumo[i]);
        } else {
            printf("Dia %d: %.2f L -> Consumo normal.\n", i + 1, consumo[i]);
        }
    }
