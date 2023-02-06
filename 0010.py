#!/usr/bin/env python3

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def isprime(num):
	for i in range(2, num):
		if num % i == 0:
			return 0
	return 1

res = 29920054136
for p in range (888959, 2000000):
	print("Nº ",p,". SUMA PRIMOS = ",res)
	if isprime(p) == 1:
		res += p
print("EL RESULTADO ES = ", res)

#PROCESING Nº 888959 SUMA 29920054136
