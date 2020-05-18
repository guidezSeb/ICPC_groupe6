#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, j;
    int test = 0;
    int A[1000];
    while(scanf("%d", &A[0]) == 1) {
        n = 1;
        if(A[0] < 0)
            break;
        while(scanf("%d", &A[n]) == 1) {
            if(A[n] < 0)
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
