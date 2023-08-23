#include <stdio.h>

int main(){
    char c;
    printf("Dando certo?\n(Y/n)\n");
    c = getchar();

    if (c == 'Y' || c == 'y'){
        printf("Uhuuul\n");
    }
    else
    printf("Chegaste aqui como?\n");
    return 0;
}
//Link para exemplo de spider no github
//https://github.com/nielssp/csol/tree/master/win