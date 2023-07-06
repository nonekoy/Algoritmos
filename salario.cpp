#include <stdio.h>

int main(){
	double salario;
	printf("Informe o seu salario:");
	scanf("%lf",&salario);
	if (salario<= 5000 & salario >0){
		salario+=1000;
	}
	printf("seu salario atualmente ficou: R$ %0.2lf", salario);
}
