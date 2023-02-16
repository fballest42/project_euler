#!/usr/bin/env python3

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

size_1num = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seveth", 8:"eight", 9:"nine"}
fdozen = {10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen", 20:"twenty"}
dozen = {20:"twenty", 30:"Thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
hundred = " hundred"


def compose_numeral(numeral, number, num):
	str_numeral = ''
	if num == 4:
		numeral.append("one thousand")
		return 
	if num == 3:
		c = int(number // 100)
		str_numeral = str(size_1num.get(c, ''))
		str_numeral = str_numeral + hundred
		num -= 1
	if num == 2:
		d = int(number)
		if d <= 20 and len(str_numeral) != 0:
			str_numeral = str_numeral + " and " + str(fdozen.get(d, ''))
		elif d > 20 and len(str_numeral) != 0:
			str_numeral = str_numeral + " and " + str(dozen.get(d, '')) + "-"
		elif d <= 20 and len(str_numeral) == 0:
			str_numeral = str(fdozen.get(d, ''))
		elif d > 20 and len(str_numeral) == 0:
			str_numeral = str(dozen.get(d, '')) + "-"
		num -= 1
	if num == 1:
		str_numeral = str_numeral + size_1num.get(number, '')
	numeral.append([str_numeral])
	print(numeral)
		

def get_number_letters(number, numerals):
	num = 0
	for i in str(number):
		num += 1
	compose_numeral(numerals, number, num)

def get_words(number):
	i = 1
	if number <= 0 or number > 1000:
		return(print("Error: only values from 1 to 1000"))
	while i <= number:
		get_number_letters(i, numerals)
		i +=1 
	letters = 0
	for i in numerals:
		letters += len(i)
	return(print("Number of letters = ", letters))

numerals = []	
get_words(25)

