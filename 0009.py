#!/usr/bin/env python3

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

a = 1
while a <= 1000 / 3:
	b = a + 1
	while (b <= 1000 / 2):
		c = 1000 - a - b
		if (a * a + b * b == c * c):
			print("LOS NUMEROS SON A= ", a, ", B= ", b, ", C= ", c, ". EL RESULTADO ES = ", a * b * c )
			break
		b = b + 1
	a = a + 1
		
