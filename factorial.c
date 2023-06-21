//Escribir un programa modular, que solicite el ingreso de un valor,
//validando que el mismo esté entre 0 y 20; y luego calcule e informe el factorial del número ingresado.
//Si el número ingresado no cumple con lo solicitado, informar y pedir el reingreso del número.
//Repetir la operación hasta que el número sea válido.

#include <stdio.h>
int ingresar_numero(){
    int numero;
    printf("Ingrese un numero entre el 0 y 20: ");
    scanf("%d", &numero);
    while(numero < 0 || numero > 20){
        printf("numero invalido Ingrese un numero entre el 0 y 20: ");
        scanf("%d", &numero);
    }

}
int factorizar(int numero){
    int factorial = 1;
    if (numero == 0) {
        factorial = 0;
    } else {
        for (int i = 1; i <= numero; i++) {
            factorial *= i;
        }
        return factorial;
    }
}

int main() {
    int numero = ingresar_numero();
    int factorial = factorizar(numero);
    printf("el factorial es: %d",factorial);
    return 0;
}