#!/usr/bin/env python
"""
Windrock Programmer's Forum #2

Challenge:

How many Sundays fell on the first of the month during the twentieth century?

Given:

* 1 Jan 1900 was a Monday.
* The twentieth century started on 1 Jan 1901 and ended on 31 Dec 2000.
* A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.
"""

# Calculate day of the week
# Python has a weekday function, but it only works for years from 1970 onward
# I chose Zeller's Rule: f = k + [(13*m-1)/5] + D + [D/4] + [C/4] - 2*C
# This works for our purposes. However, it is worth noting that it only works for the Gregorian calendar
def day_of_week(day, month, year):
    yr = year
    if month > 2:
        m = month - 2
    else:
        m = month + 10
        yr = yr - 1
    D = yr % 100;
    C = int(yr / 100);
    value = (day + int((13*m-1)/5) + D + int(D/4) + int(C/4) - 2*C) % 7
    return value

# Main program
months=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sunday_count = 0
for yr in range(1901, 2001):
    for mo in range(1, 13):
        if day_of_week(1, mo, yr) == 0:
            print "01 " + months[mo-1] + " " + str(yr)
            sunday_count += 1
print
print "Found " + str(sunday_count) + " Sunday(s) on the first of the month from 1-Jan-1901 to 31-Dec-2000.\n"
