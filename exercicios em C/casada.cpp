#include <stdio.h>

int main(){
double salario; 
double imposto;
char casado;
bool test= true;

printf("Digite o seu salario:");
scanf("%lf",&salario);

while (test == true){
printf("qual o seu estado civil:\n");
printf("casado digite 'C' solteiro digite 'S',\n");
printf("ou 'D' para divorciado :  ");
scanf("%s", &casado);
if (casado == 'c' || casado == 'C'){
	imposto = salario*0.1;
	printf("seu imposto a ser pago : R$%0.2lf",imposto);
	test = false;
}else{if (casado == 's' || casado == 'S'){
	imposto = salario*0.05;
	printf("seu imposto a ser pago : R$ %0.2lf", imposto);
	test = false;
}else{if(casado == 'd'|| casado =='D'){
	imposto = salario*0.05;
	printf("seu imposto a ser pago : R$ %0.2lf", imposto);
	test = false;
}else{printf("Algum valor foi incorreto.");
}	
}
}
}
}

