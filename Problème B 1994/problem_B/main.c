#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, j;
    int test = 0;
    int buff[1000];
    while(scanf("%d", &buff[0]) == 1) {
        n = 1;
        if(buff[0] < 0)
            break;
        while(scanf("%d", &buff[n]) == 1) {
            if(buff[n] < 0)
                break;
            else
                n++;
        }
        if(test)
            printf("test");
        printf("Test #%d:\n", ++test);

    }
    return 0;
}
