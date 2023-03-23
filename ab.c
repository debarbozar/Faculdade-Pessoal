#include <stdio.h>
#include <stdlib.h>
#define MAX 10
#define MEDIA 7

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int menu() {
    int opcao; 
    system("cls");

    printf("\n(1) Digitar as 10 notas");
    printf("\n(2) Visualizar notas");
    printf("\n(3) Calcular media");
    printf("\n(4) Obter maior nota");
    printf("\n(5) Obter menor nota");
    printf("\n(6) Percentual acima da media (Maior que 7)");
    printf("\n(7) Sair");
    printf("\n\n Digite uma opcao: ");

    scanf("%d", &opcao);
    return opcao;
}

//funcao sem retorno
void inserir_notas(float* notas) {
	int i;
    system("cls");

    for (i=0; i < MAX; i++) {
        printf("\n Informe a nota %d: ", i+1);
        scanf("%f", &notas[i]);
    }
}

//vetor
void visualizar_notas(float *notas)
{
    int i;

    for (i = 0; i < MAX; i++) {
        printf("\n Nota %d: %.2f", i+1, notas[i]);
    }
}

float calcular_media(float *notas) {
    int i;
    float contador = 0, notaMedia = 0;

    for (i = 0; i < MAX; i++) {
        contador += notas[i];
    } 

    notaMedia = contador / MAX;
    return notaMedia;
}

float obter_maior_nota(float *notas, float maiorNota)
{
	int i;
    for (i = 0; i < MAX; i++)
    {
        if (i == 0)
        {
            maiorNota = notas[0];
        }
        else
        {
            if (notas[i] > maiorNota)
            {
                maiorNota = notas[i];
            }
        }
    }

    return maiorNota;
}

float obter_menor_nota(float *notas, float menorNota)
{
	int i;
    for (i = 0; i < MAX; i++)
    {
        if (i == 0)
        {
            menorNota = notas[0];
        }
        else
        {
            if (notas[i] < menorNota)
            {
                menorNota = notas[i];
            }
        }
    }

    return menorNota;
}

float calcular_percentual_de_aprovacao(float *notas) {
    int i;
    float media = 0, acimaDaMedia = 0;

    for (i = 0; i < MAX; i++) {
        if (notas[i] >= MEDIA)
            acimaDaMedia++;
    }
    return (acimaDaMedia / MAX) * 100;

}

int main() {

    int opcao, tamanho;
    float notas[MAX], maior = 0, menor = 0, percentual = 0, media = 0;

    do {
        opcao = menu();

        switch (opcao) {
            case 1:
                inserir_notas(notas);
                break;
            case 2:
	            visualizar_notas(notas);
	            break;

	        case 3:
	            media = calcular_media(notas);
	            printf("A media das notas eh %.2f", media);
	            break;
	        
            case 4:
	            maior = obter_maior_nota(notas, maior);
	            printf("A maior nota eh %.1f", maior);
	            break;
	            
	        case 5: 
	            menor = obter_menor_nota(notas, menor);
	            printf("A menor nota eh %.1f", menor);
	            break;
	            
	        case 6:
	            percentual = calcular_percentual_de_aprovacao(notas);
	            printf("O percentual de aprovacao foi de %.2f", percentual);
	            break;
	            
	        case 7:
	        	exit(1);
	        default:
	            system("cls");
	            printf("\n Opcao invalida");

        }
		
		getch();

    } while (opcao != 7);

    return 0;
}

