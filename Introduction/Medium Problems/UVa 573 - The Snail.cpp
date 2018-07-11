#include <stdio.h>

int main(){
    int height, up, slide, porcentage;
    double decrease, current;
    while(1){
        scanf("%d %d %d %d", &height, &up, &slide, &porcentage);
        if(height == 0) break;
        decrease = ((double)porcentage)/100;
        current = 0.0;
        int ite = 0;
        double temp;
        while(1){
            temp = ((double)up) - ((double)(up*ite))*decrease;
            if(temp <= 0) temp = 0;
            current += temp;          
            if(current > height){
                printf("success on day %d\n", ite+1);
                break;
            }
            current -= slide;
            if(current < 0){
                printf("failure on day %d\n", ite+1);
                break;
            }
            ite++;
        }
    }
    return 0;
}