/*Definir una función recursiva en C que recibe un vector de enteros por parámetro, su tamaño y 
devuelve la productoria de los valores (producto de todos sus valores).
int productoria(int vec[], int n);
*/
#include <stdio.h>

int productoria(int vec[], int n){
    if(n == 0){
        return 1;
    }
    else{
        return vec[n-1] * productoria(vec, n-1);
    }
}


int main(){
    int vector[] = {1, 4, 3, 6, 7};
    int large = sizeof(vector)/sizeof(vector[0]);
    int resultado = productoria(vector, large);
    printf("el resultado es %i", resultado);
    return 0;
}