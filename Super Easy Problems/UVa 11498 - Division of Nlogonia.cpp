#include <stdio.h>

int main(){
    int N, mx, my, px, py, i;
    while(1){
        scanf("%d", &N);
        if (N == 0) break;
        scanf("%d %d", &mx, &my);
        while(N--){
            scanf("%d %d", &px, &py);            
            if(mx == px || my == py)
                printf("divisa\n");
            else if(py > my && px > mx)
                printf("NE\n");
            else if(py > my && px < mx)
                printf("NO\n");
            else if(py < my && px > mx)
                printf("SE\n");
            else
                printf("SO\n");
        }
    }
    return 0;
}