#!/usr/bin/env python3

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

size_1num = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seveth", 8:"eight", 9:"nine"}
fdozen = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
dozen = {20:"twenty", 30:"Thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
hundred = " hundred"


def compose_numeral(numeral, number, num):
	str_numeral = ""
	if num == 4:
		numeral.append("one thousand")
	elif num == 3:
		str_numeral = size_1num.get(str(number)[0])
		# str_numeral = str_numeral + hundred
		numeral.append(str_numeral)
	elif num == 2:
		numeral.append("AA")
	elif num == 1:
		numeral.append("A")
		

def get_number_letters(number):
	num = 0
	numerals = []
	letters = 0
	if number <= 0 or number > 1000:
		return(print("Error: only values from 1 to 1000"))
	while number >= 10:
		for i in str(number):
			num += 1
		print(num)
		number = int(number // 10)
		compose_numeral(numerals, int(number), num)
	i = 1
	for i in numerals:
		letters += len(i)
	return(print("Number of letters = ", letters))
	
get_number_letters(111)

