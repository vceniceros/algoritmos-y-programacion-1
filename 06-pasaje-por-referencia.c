#include <stdio.h>

void cumplir_anios(int* edad) {
    *edad = *edad+1;
}

int main() {
    int edad;
    printf("Ingrese su edad: ");
    scanf("%d", &edad);

    cumplir_anios(&edad);
    printf("Feliz cumpleanios! Ahora tenes %d anios---!\n", edad);
    saludar();
    return 0;
}
