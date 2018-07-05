#include <stdio.h>

int main(){
    int T, num, res, temp, i, j;
    scanf("%d", &T);
    for(i = 0; i < T; i++){
        scanf("%d", &num);
        for(j = 0; j < num; j++){
            scanf("%d", &temp);
            if(!j)
                res = temp;
            else if(temp > res)
                res = temp;
        }
        printf("Case %d: %d\n", i+1, res);
    }
    return 0;
}