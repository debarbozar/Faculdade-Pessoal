#include <stdio.h>
#include <stdlib.h>

#define MAX 10

//Procedimento
void ler_vetor(float* meuVet,int* qtd_nums){
	int i;
	printf("\nInforme quantos numeros voce deseja manipular: ");
	scanf("%d",qtd_nums); //Ja estamos recebendo o endereço de qtd (nao precisa de &)
	for(i=0;i<*qtd_nums;i++){
		printf("numeros[%d]: ",i);
		scanf("%f",&meuVet[i]);
	}
}

//Procedimento
void imprimir_vetor(float* meuVet,int qtd_nums){
	int i;	
	for(i=0;i<qtd_nums;i++){
		printf("\nnumeros[%d]: %.2f",i,meuVet[i]);		
	}
}

//Função
float soma_elementos_vetor(float* meuVet, int qtd_nums){
	int i;	
	float soma_elementos = 0;
	for(i=0;i<qtd_nums;i++){
		soma_elementos += meuVet[i];
	}
	return soma_elementos;
}

int main(int argc, char *argv[]) {
	float numeros[MAX];
	int qtd = 0;
	ler_vetor(numeros,&qtd); // qtd eh passado por referência
	printf("\nQTD = %d",qtd); 
	imprimir_vetor(numeros,qtd); //qtd eh passado por valor (copia qtd para a área de stack)
	
	float soma = soma_elementos_vetor(numeros,qtd);
	printf("\nA soma dos elementos do vetor eh igual a %.2f",soma);
	
	ler_vetor(numeros,&qtd); 
	printf("\nQTD = %d",qtd); 
	imprimir_vetor(numeros,qtd);
		
	printf("\nA soma dos elementos do vetor eh igual a %.2f",soma_elementos_vetor(numeros,qtd));
	
	return 0;
}
