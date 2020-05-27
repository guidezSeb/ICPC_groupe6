#include <stdio.h>
#include <string.h>

int sol;
char path[1024];

void checkSum(int *place, int sum, char expr[], int index)
{
	for (int i = 0; i < index; i++)
		sum += place[i];
	if (sum == 2000)
	{
		printf("  %s=\n", expr);
		sol++;
	}
}

void calculSol(char expr[])
{
	int n = 0;
	int place[20];
	int index = 0;
	char oper = '+';
	int sum = 0;
	n = strlen(expr);
	for (int i = 0; i < n;)
	{
		if (expr[i] >= '0' && expr[i] <= '9')
		{
			int num = 0;
			if (expr[i] == '0' && expr[i + 1] >= '0' && expr[i + 1] <= '9')
				return;
			while (expr[i] >= '0' && expr[i] <= '9')
			{
				num = num * 10 + expr[i] - '0';
				i++;
			}
			if (oper == '*')
				place[index - 1] *= num;
			else if (oper == '-')
				place[index++] = -num;
			else if (oper == '+')
				place[index++] = num;
		}
		else
		{
			oper = expr[i];
			i++;
		}
	}
	checkSum(place, sum, expr, index);
}

void defIndex(int index, int place, int n, char *stop)
{
	char operator[] = "*+-";
	if (index == n)
	{
		path[place] = '\0';
		if (place > n)
			calculSol(path);
		return;
	}
	if (index != n - 1)
	{
		for (int i = 0; i < 3; i++)
		{
			path[place] = stop[index];
			path[place + 1] = operator[i];
			defIndex(index + 1, place + 2, n, stop);
		}
	}
	path[place] = stop[index];
	defIndex(index + 1, place + 1, n, stop);
}

int main()
{
	int n;
	int cases = 0;
	char stop[1024];
	printf("Veuillez rentrer une operation ou rentrer = pour quitter\n");
	while (scanf("%s", stop) == 1)
	{
		if (!strcmp(stop, "="))
			break;
        sol = 0;
		n = strlen(stop);
		stop[n - 1] = '\0';
		n--;
		printf("Probleme %d\n", ++cases);
		defIndex(0, 0, n, stop);
		if (sol == 0)
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
