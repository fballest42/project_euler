#!/usr/bin/env python3

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

b = 0
for i in range(111, 999):
	for j in range(111, 999):
		a = i * j
		if str(a) == str(a)[::-1] and a < b:
			b = a
