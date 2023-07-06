#include <stdio.h>

int main(){
	double salario; double imposto;
	printf("Digite seu salario para checar seu imposto:");
	scanf("%lf",&salario);
	if (salario <= 0){
		printf("Salario invalido.");
	}else{if(salario <= 1000){
		imposto = salario * 0.05;
	}else{
		imposto = salario * 0.1;
	}printf("O imposto a ser pago sera : R$ %0.2lf", imposto);
	}
	
}
