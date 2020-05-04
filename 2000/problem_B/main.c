#include <stdio.h>
#include <string.h>


void calculSol(char expr[]) {
//faire l operation
}

void defIndex(int index, int place, int n, char *s) {
    char path[1024];
	char operator[] = "*+-";
	if (index == n) {
		path[place] = '\0';
		if (place > n)
		//calculSol(path);
		return ;
	}
	if (index != n-1) {
	for (int i = 0; i < 3; i++) {
			path[place] = s[index], path[place + 1] = operator[i];
			defIndex(index+1, place+2, n,s);
		}
	}
	path[place] = s[index];
	defIndex(index+1, place +1, n,s);
}

int main() {
	int sol,n;
	int cases = 0;
char s[1024];
	while (scanf("%s", s) == 1) {
		if (!strcmp(s, "="))
			break;
		n = strlen(s);
		s[n - 1] = '\0';
		sol = 0;
		printf("Problem %d\n", ++cases);
		n--;
		defIndex(0, 0, n,s);
		if (sol == 0)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
