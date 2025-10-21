#include <stdio.h>

#define PERSONAS 4
#define SEMANAS 4
#define DIAS 7

int main() {
    int i, j, k;
    float ejercicio[PERSONAS][SEMANAS][DIAS];
    float totalPersona[PERSONAS] = {0};
    float totalSemana[SEMANAS] = {0};
    float promedioSemanal[PERSONAS][SEMANAS];
    float variacionPersona[PERSONAS];
    int personaMasConstante = 0;
    float menorVariacion = 999999.0;

    printf("=== SEGUIMIENTO DE ACTIVIDAD FÍSICA FAMILIAR ===\n");

    // Entrada de datos
    for(i = 0; i < PERSONAS; i++) {
        printf("\n--- Persona %d ---\n", i + 1);
        for(j = 0; j < SEMANAS; j++) {
            printf(" Semana %d:\n", j + 1);
            for(k = 0; k < DIAS; k++) {
                printf("  Minutos de ejercicio día %d: ", k + 1);
                scanf("%f", &ejercicio[i][j][k]);
            }
        }
    }

    // Calcular totales y promedios
    for(i = 0; i < PERSONAS; i++) {
        for(j = 0; j < SEMANAS; j++) {
            float sumaSemana = 0;
            for(k = 0; k < DIAS; k++) {
                sumaSemana += ejercicio[i][j][k];
                totalSemana[j] += ejercicio[i][j][k];
            }
            promedioSemanal[i][j] = sumaSemana / DIAS;
            totalPersona[i] += sumaSemana;
        }
    }

    // Mostrar total y promedio semanal por persona
    printf("\n=== TOTAL Y PROMEDIO SEMANAL POR PERSONA ===\n");
    for(i = 0; i < PERSONAS; i++) {
        printf("\nPersona %d:\n", i + 1);
        printf(" Total mensual: %.2f minutos\n", totalPersona[i]);
        for(j = 0; j < SEMANAS; j++) {
            printf("  Semana %d - Promedio diario: %.2f min/día\n", j + 1, promedioSemanal[i][j]);
        }
    }

    // Calcular variación (consistencia)
    printf("\n=== CONSISTENCIA EN EJERCICIO ===\n");
    for(i = 0; i < PERSONAS; i++) {
        float sumaVar = 0;
        int contador = 0;

        for(j = 0; j < SEMANAS; j++) {
            float mediaSemana = promedioSemanal[i][j];
            for(k = 0; k < DIAS; k++) {
                float diferencia = ejercicio[i][j][k] - mediaSemana;
                if(diferencia < 0) diferencia = -diferencia; // valor absoluto sin math.h
                sumaVar += diferencia;
                contador++;
            }
        }

        variacionPersona[i] = sumaVar / contador;

        printf("Persona %d - Variación promedio: %.2f\n", i + 1, variacionPersona[i]);

        if(variacionPersona[i] < menorVariacion) {
            menorVariacion = variacionPersona[i];
            personaMasConstante = i;
        }
    }

    printf("\nLa persona más constante es la Persona %d (variación promedio: %.2f)\n", 
           personaMasConstante + 1, menorVariacion);

    // Semana con mayor actividad total
    int semanaMax = 0;
    float mayorSemana = totalSemana[0];
    for(j = 1; j < SEMANAS; j++) {
        if(totalSemana[j] > mayorSemana) {
            mayorSemana = totalSemana[j];
            semanaMax = j;
        }
    }

    printf("\nLa semana con mayor actividad familiar fue la Semana %d (%.2f minutos en total)\n",
           semanaMax + 1, mayorSemana);

    return 0;
}
