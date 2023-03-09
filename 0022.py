#!/usr/bin/env python3

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
# five-thousand first names, begin by sorting it into alphabetical order. 
# Then working out the alphabetical value for each name, multiply this value by its alphabetical 
# position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order,
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
# name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

def get_names():
	names = []
	sum = 0
	val = 0
	with open('p022_names.txt', 'r+') as file:
		for lines in file:
			names.append((lines.replace('"', '').split(',')))
		names = sorted(names[0])
		for x, nm in enumerate(names, 1):
			for letter in nm:
				val = val + ord(letter) - 64
			sum = sum + (x * val)
			val = 0
	return sum

print("THE RESULT IS = ", get_names())
