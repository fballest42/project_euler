#!/usr/bin/env python3

# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

import math

def factorial_sumatory(ret, num):
	for nm in str(math.factorial(num)):
		ret = int(nm) + ret
	return ret

print("SUM = ", factorial_sumatory(0, 100))
