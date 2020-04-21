#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define eps 1e-6

int main() {
    int cas = 0;
    int n, m, A[1058];
    double V, h= 0, sum = 0;

    while (scanf("%d %d", &n ,&m) == 2) {
         if (n < 30 && m < 30){
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                scanf("%d", &A[i*m+j]);
        scanf("%lf", &V);
        printf("0 0\n");
        n = n*m;
        A[n] = 1*exp(10);
        printf("Region %d\n", ++cas);
        for (int i = 0; i < n; i++) {
            sum += A[i];
            h = (V+sum*100)/(i+1)/100.0;
            if (h < A[i+1]+eps) {
                printf("Water level is %.2lf meters.\n", h);
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
