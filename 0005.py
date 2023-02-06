#!/usr/bin/env python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

j = 20
prime = [2,3,5,7,11,13,17,19]
k = 1
for i in prime:
	l = i
	while l <= j:
		k *= i
		l = l * i
		print(k)
print("EL NUMERO ES: ", k)
