#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define eps 1e-6

int main() {
    int cas = 0;
    int n, m, A[1058];
    double volCub,lastLine, waterLev= 0, sum = 0;

    while (scanf("%d %d", &n ,&m) == 2) {
         if (n < 30 && m < 30){
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &A[i*m+j]);
        scanf("%lf", &volCub);
        scanf("%lf", &lastLine);
        n = n*m;
        A[n] = 1*exp(10);
        printf("\nRegion %d\n", ++cas);
        for (int i = 0; i < n; i++) {
            sum += A[i];
            waterLev = (volCub+sum*100)/(i+1)/100.0;
            if (waterLev < A[i+1]+eps) {
                printf("Water level is %.2lf meters.\n", waterLev);
                printf("%.2lf percent of the region is under water.\n\n", (i+1)*100.0/n);
                break;
            }
        }
    }
    else{
      printf("can you give us a pair which is less than 30 please\n");
    }
    }

    return 0;
}
