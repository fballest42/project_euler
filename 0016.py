#!/usr/bin/env python3

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?


def digits_sum_number(num, exp):
	power = pow(num, exp)
	res = 0
	for i in str(power):
		res += int(i)
	print("RESULT = ", res)

digits_sum_number(2, 1000)
