#include<stdio.h>

// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143 ?

int main()
{
	unsigned long long y;
	unsigned long long num = 600851475143;
	unsigned long long j;
	int prime = 0;
	for(y = 2; y <= num; y++){
		if (num % y == 0)
		{
			prime = 1;
			for(j = 2; j <= y / 2; j++)
			{
				if (y % j == 0)
				{
					prime = 0;
					break;
				}
			}
			if (prime == 1)
				printf("%llu\n",  y);
		}
	}
	return (0);
}
