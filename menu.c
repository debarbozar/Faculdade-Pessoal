#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 10

int menu() {
    int opcao; 
    system("cls");

    printf("\n(1) Digitar as 10 notas");
    printf("\n(2) Visualizar notas");
    printf("\n(3) Calcular média");
    printf("\n(4) Obter maior nota");
    printf("\n(5) Obter menor nota");
    printf("\n(6) Percentual acima da média (Maior que 7)");
    printf("\n(7) Sair");
    printf("\n\n Digite uma opcao: ");

    scanf("%d", &opcao);
    return opcao;
}

void inserir_notas(float* notas) {
	int i;
    system("cls");

    for (i=0; i < MAX; i++) {
        printf("\n Informe a nota %d: ", i+1);
        scanf("%f", &notas[i]);
    }
}



int main() {

    int opcao; 
    float notas[MAX];

    do {
        opcao = menu();

        switch (opcao) {
            case 1:
                inserir_notas(notas);
                break;

        }


    } while (opcao != 7);

    return 1;
}

