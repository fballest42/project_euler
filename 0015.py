#!/usr/bin/env python3

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# look at image15.png file to description of routes

# How many such routes are there through a 20×20 grid?

def fact_number(number):
	fact_num = number
	while (number > 1):
		fact_num = fact_num * (number - 1)
		number -= 1
	return fact_num

def routes_number(alto, ancho):
	num = (alto + ancho)
	fact_num = fact_number(num)
	options = fact_number(alto)
	variations = fact_num // (options * fact_number(num - alto))
	print("VARIACIONES = ", variations)

routes_number(20, 20)
# routes_number(20, 20)
