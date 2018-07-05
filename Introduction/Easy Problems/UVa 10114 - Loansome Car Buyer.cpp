#include <stdio.h>

int main(){
    int months, inputs, i, j;
    double payment, total, por;
    while(1){
        scanf("%d %lf %lf %d", &months, &payment, &total, &inputs);       
        if(months < 0) break;
        double array_months[101];
        int num;
        for(i = 0; i < inputs; i++){
            scanf("%d %lf", &num, &por);
            for(j = num; j < 101; j++)
                array_months[j] = por;
        }
        i = 0;
        double pay = total/months, value = (total+payment)*(1-array_months[i]);
        while(value < total){
            i++;
            value = value * (1-array_months[i]);
            total -= pay;
        }
        if(i == 1)
            printf("1 month\n");
        else
            printf("%d months\n", i);
    }
    return 0;
}