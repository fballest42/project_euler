#include<unistd.h>
#include<stdio.h>

// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Find the sum of all the multiples of 3 or 5 below 1000.

int main()
{
	int i = 0, cont = 0;

	while(i < 1000)
	{
		if (i % 3 == 0 || i % 5 == 0)
			cont += i;
		i++;
	}
	printf("EL RESULTADO ES: %d\n", cont);
	return (0);
}
