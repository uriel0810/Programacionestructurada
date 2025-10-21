#include <stdio.h>

int main() {
    float a;
    float b;
    float area;
    printf("ingresa pi ");
    scanf("%f",&a);
    printf("ingresa el radio ");
    scanf("%f",&b);
    area=a * b*b ;
    printf("el resultado es %f\n",area);

    return 0;
}