#include <stdio.h>

int main(){
    long long int i, a, b;
    scanf("%lld", &i);
    while(i--){
        scanf("%lld %lld", &a, &b);
        if(a < b)
            printf("<\n");
        else if(a > b)
            printf(">\n");
        else 
            printf("=\n");
    }
    return 0;
}