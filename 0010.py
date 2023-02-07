#!/usr/bin/env python3

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def isprime(num, lst):
	for i in lst:
		if num % i == 0:
			return 0
	for i in range(int(lst[-1]), num, 2):
		if num % i == 0:
			return 0
	return 1
	
res = 0
lst = [2]
for p in range (3, 2000000, 2):
	if isprime(p, lst) == 1:
		lst.append(p)
		print(p)
for n in lst:    
	res += n
print("LA LST=", lst, "EL RESULTADO ES = ", res)

#Nº 142853828922 ERROR
