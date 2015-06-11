#!/usr/bin/env python

def leap(year):
    return year % 400 == 0 or \
        (year % 4 == 0 and year % 100)

day_name = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

year = 1900
day = 1

month_regs = [31,28,31,30,31,30,31,31,30,31,30,31]
month_leap = [31,29,31,30,31,30,31,31,30,31,30,31]

first_sundays = []

while year <= 2000:
    months = month_leap if leap(year) else month_regs
    for i in range(len(months)):
        if day % 7 == 0: first_sundays.append((year, i+1))
        day = day + months[i]
    year = year + 1

print len([e for e in first_sundays if e[0] >= 1901])
