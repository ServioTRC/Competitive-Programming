#include <stdio.h>
#include <algorithm>

int main(){
    int N, i, j, array[3];
    scanf("%d", &N);
    for(int i = 1; i <= N; i++){
        for(j = 0; j < 3; j++) scanf("%d", &array[j]);
        std::sort(array, array+3);
        printf("Case %d: %d\n", i, array[1]);
    }
    return 0;
}