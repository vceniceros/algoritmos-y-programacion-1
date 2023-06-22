#include <stdio.h>
#include <stdio.h>
int productoria(int vec[],  int n){
    if(n == 0){
        return 1;
    }
    else{
        return vec[n-1] * productoria(vec, n-1);
    }
}
int main()
{
    int vec1[] = {1, 5, 6, 7, 9};
    int tamano = sizeof(vec1) / sizeof(vec1[0]);
    int resultado = productoria(vec1, tamano);
    printf("resultado es %i", resultado);
    return 0;
}
