#include <stdio.h>

int main(){
	int num;
	printf("Digite o numero a ser checado:");
	scanf("%d",&num);
	if (num == 0){
		printf("O numero digitado foi zero.");
	}else{
		printf("O numero digitado foi %d.", num);
	}
}
