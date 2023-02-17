#!/usr/bin/env python3

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.

size_1num = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen"}
dozen = {20:"twenty", 30:"thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}
hundred = " hundred "


def compose_numeral(numerals, number, num):
	if num == 4:
		numerals.append("one thousand")
		return
	c = int(number // 100)
	d = int((number - (c * 100)) // 10)
	u = int((number - ((c * 100) + (d * 10))))
	str_numeral = '' 
	if num == 3:
		str_numeral = str(size_1num.get(c, ''))
		str_numeral = str_numeral + hundred
		num -= 1
	if num <= 2:
		if (d * 10 + u) <= 19 and len(str_numeral) > 0:
			if d == 0 and u == 0:
				str_numeral = str_numeral + str(size_1num.get(u, ''))
			else:
				str_numeral = str_numeral + "and " + str(size_1num.get(d * 10 + u, ''))
		elif (d * 10) > 19 and len(str_numeral) > 0:
			if u != 0:
				str_numeral = str_numeral + "and " + str(dozen.get(d * 10)) + '-' + str(size_1num.get(u))
			else:
				str_numeral = str_numeral + "and " + str(dozen.get(d * 10))
		elif (d * 10 + u) <= 19 and len(str_numeral) == 0:
			str_numeral = str(size_1num.get(d * 10 + u))
		elif (d * 10 + u) > 19 and len(str_numeral) == 0:
			if u != 0:
				str_numeral = str(dozen.get(d * 10)) + '-' + str(size_1num.get(u))
			else:
				str_numeral = str(dozen.get(d * 10))
	numerals.append([str_numeral])
		

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
	letters = ''
	for i in range(0, number):
		letters += ''.join(((str(numerals[i]).strip("['")).strip("']")).split(' '))
	letters = ''.join(letters.split('-'))
	return(print("Number of letters = ", len(letters)))

numerals = []	
get_words(1000)

