#include <stdio.h>

int cumplir_anios(int a) {
    return a + 1;
}

int main() {
    int edad;
    int nueva_edad;

    printf("Ingrese su edad: ");
    scanf("%d", &edad);

    nueva_edad = cumplir_anios(edad);
    printf("Feliz cumpleanios! Ahora tenes %d anios!\n", nueva_edad);
    return 0;
}
