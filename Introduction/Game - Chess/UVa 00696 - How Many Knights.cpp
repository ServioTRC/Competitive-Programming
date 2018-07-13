#include <stdio.h>
#include <cmath>

int main(){
    int m, n, res;
    while(true){
        scanf("%d %d", &m, &n);
        if(m == 0 && n == 0) break;

        if(m == 1 || n == 1) res = m*n;
        else if(m == 2 && n == 2) res = m*n;
        else {
            if(m == 2 || n == 2){
                if(m % 4 == 0 || n % 4 == 0) 
                    res = (int) ceil(((double)(m*n))/2.0);
                else{
                    if(m == 2){
                        res = ((n/2) * 2) + 2;
                    } else if(n == 2){
                        res = ((m/2) * 2) + 2;
                    }
                }
            } else res = (int) ceil(((double)(m*n))/2.0);
        }
        printf("%d knights may be placed on a %d row %d column board.\n", res, m, n);
    }
    return 0;
}