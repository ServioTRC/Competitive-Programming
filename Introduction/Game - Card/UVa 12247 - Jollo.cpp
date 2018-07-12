#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <iterator>
#define length(x) (sizeof(x)/sizeof(*x))

bool contains(int *cards, int val){
    for(int i = 0; i < 5; i++){
        if(cards[i] == val)
            return true;
    }
    return false;
}

int main(){
    int i, j, cards[5], princess[3], prince[2], loss, election;
    bool loss1, loss2;
    while(1){
        for(i = 0; i < 5; i++){
            scanf("%d", &cards[i]);
        }
        if(cards[0] == 0) break;
        for(i = 0; i < 5; i++){
            if(i < 3)
                princess[i] = cards[i];
            else{
                prince[i-3] = cards[i];
            }
        }
        std::sort(princess, princess+3);
        std::reverse(princess, princess+3);
        std::sort(prince, prince+2);
        std::reverse(prince, prince+2);
        loss = 0;
        loss1 = false;
        loss2 = false;        
        for(i = 0; i < 3; i++){
            for(j = 0; j < 2; j++){
                if(princess[i] > prince[j]){
                    loss++;
                    if(i == 0 && j == 0) loss1 = true;
                    else if(i == 1 && j == 1) loss2 = true;
                } 
            }
        }

        if(loss1 && loss2){
            printf("-1\n");
            continue;
        }

        if(loss == 0) election = 1;
        else if(loss1){
            if(loss == 2) election = princess[1] + 1;
            else election = princess[0] + 1;
        }
        else{
            if(princess[1] < prince[1])
                election = princess[1]+1;
            else
                election = princess[0]+1;            
        }

        int error = 0;
        while(1){
            if(election > 52){
                error = 1;
                break;
            }

            if(contains(cards, election)) election++;
            else break;            
        }
        if(error) printf("-1\n");
        else printf("%d\n", election);
    }
    return 0;
}