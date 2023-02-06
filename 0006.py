#!/usr/bin/env python3

# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def squaressum(num):
	k = 0
	for i in range(num):
		k = i * i
	print("K* -> ", k, "  i es=", i)
	return k

def sumsquare(num):
	k = 0
	for i in range(num):
		k += i
	print("K+ -> ", k, "  i es=", i)
	k *= k
	return k

a = 0
b = 0
for i in range (1, 102):
	a += squaressum(i)
	b = sumsquare(i)
c = b - a
print("RESULTADO = ", c)
