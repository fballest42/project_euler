#!/usr/bin/env python3


# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import calendar

def get_sundays():
	ret = 0
	for yy in range(1901, 2001):
		for mm in range(1, 13):
			month = calendar.monthcalendar(yy,mm)
			if int(month[0][6]) == 1:
				ret += 1
	print("SUNDAYS = ", ret)

get_sundays()
