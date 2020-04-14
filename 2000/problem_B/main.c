#include <stdio.h>
#include <string.h>

char s[1024];

void dfs(int index, int pl, int n) {
	//char operator[] = "*+-";
	if (index == n) {
	//check
	}
	if (index != n-1) {
	//recursif
	}
	dfs(index+1, pl+1, n);
}

int main() {
	int n, sol;
	int cases = 0;

	while (scanf("%s", s) == 1) {
		if (!strcmp(s, "="))
			break;
		n = strlen(s);
		s[n - 1] = '\0';
		n--;
		sol = 0;
		printf("Problem %d\n", ++cases);
		dfs(0, 0, n);
		if (sol == 0)
			printf("IMPOSSIBLE");
	}
	return 0;
}
