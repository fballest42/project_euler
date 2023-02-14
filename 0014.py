#!/usr/bin/env python3

# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# Once the chain starts the terms are allowed to go above one million.

def chainmaker(num):
	chain = []
	chain.append(num)
	while num > 1:
		if num % 2 == 0:
			num = num // 2
		else:
			num = num * 3 + 1
		chain.append(num)
	return chain

def checknumbers(num):
	i = 0
	max_size = 0
	chains = []
	while i < num:
		chains.append(chainmaker(i))
		if max_size < len(chains[i]):
			max_size = len(chains[i])
			numero = i
		i += 1
		print("TESTING....", i)
	print("NUMBER: ", numero, "SIZE: ", max_size
	)
checknumbers(1000000)
