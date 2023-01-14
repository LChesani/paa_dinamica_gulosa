#include <stdio.h>
int main(void){ //basicamente
    for(int i = 0, n; scanf("%d", &n) && n; i++){  
        int max = 1, arr[n], sizes[n]; //size é o vetor dinamico, pode ser usado para ver os "maiores provisorios" ao final também
        for(int i = 0; i < n; i++){
            scanf(" %d", &arr[i]);
            sizes[i] = 1; //minimo 1
        }
        for(int i = 0; i < n; i++)
            for(int j = 0; j < i; j++) //compara do inicio até o i
                if(arr[i]>arr[j] && sizes[i]<sizes[j]+1){ //aqui e onde ele compara e acontece a magica do dinamico
                    sizes[i] = sizes[j] + 1; //armazena o tamanho da subsequencia
                    if(max < sizes[i]) max = sizes[i]; //atualiza o tamanho maximo
                }
        printf("%d : %d\n", i, max);
    }
}