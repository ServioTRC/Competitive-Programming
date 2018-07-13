#include <stdio.h>
#include <cmath>

int min(int x, int y){
    if(x < y)
        return x;
    else
        return y;
}

int knights(int m, int n){
    int res;
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
    return res;
}

int main(){
    int cases, m, n, i, res;
    double m1, n1;
    char type;
    scanf("%d", &cases);
    for(i = 0; i < cases; i++){
        scanf(" %c %d %d", &type, &m, &n);
        switch(type){
            case 'r':
                //Rook
                res = min(m, n);
                break;
            case 'k':
                //Knight
                res = knights(m,n);
                break;
            case 'Q':
                //Queen
                res = min(m, n);
                break;
            case 'K':
                //King
                m = (int) ceil((double)m / 2.0);
                n = (int) ceil((double)n / 2.0);
                res = m*n;
                break;
        }
        printf("%d\n", res);
    }
    return 0;
}