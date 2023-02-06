#!/usr/bin/env python3

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

def isprime(num):
	for i in range(2, num):
		if num % i == 0:
			return 0
	return 1

j = 0
k = 1
for p in range (2, 1000000000):
	if isprime(p) == 1:
		j += 1
		k = p
	if j == 10001:
		print("EL NUMERO ES = ", k)
		break
