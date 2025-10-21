#include <stdio.h>

int main() {
    char modo;

    printf("Ingrese el modo (A-automatico, M-manual, S-seguro): ");
    scanf(" %c", &modo);  // El espacio antes de %c evita problemas con el buffer

    if (modo == 'A' || modo == 'a') {
        printf("Modo automatico activado.\n");
    } 
    else if (modo == 'M' || modo == 'm') {
        printf("Modo manual activado.\n");
    } 
    else if (modo == 'S' || modo == 's') {
        printf("Modo seguro activado.\n");
    } 
    else {
        printf("Error: Modo invalido.\n");
    }

    return 0;
}
