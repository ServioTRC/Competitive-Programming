#include <stdio.h>

int main(){
    int parti, budget, hotels, weeks, i, j, min, total, cost, days;
    bool available;
    while(scanf("%d %d %d %d", &parti, &budget, &hotels, &weeks) != EOF){
        min = 0;
        for(i = 0; i < hotels; i++){
            scanf("%d", &cost);
            total = cost*parti;
            available = false;
            for(j = 0; j < weeks; j++){
                scanf("%d", &days);
                if(days >= parti)
                    available = true;
            }
            if(available && total <= budget){
                if(min == 0)
                    min = total;
                else if(total < min)
                    min = total;
            }
        }
        if(min != 0)
            printf("%d\n", min);
        else
            printf("stay home\n");
    }
    return 0;
}