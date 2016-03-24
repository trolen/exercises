#!/usr/bin/env python

from datetime import date
import re

def split_date_str(date_str):
    p = re.compile(r'[ -/]')
    (n1, n2, n3) = p.split(date_str, 3)
    return (int(n1), int(n2), int(n3))

def get_date_tuple(arg):
    if isinstance(arg, basestring):
        return split_date_str(arg)
    if isinstance(arg, (list, tuple)):
        return (arg[0], arg[1], arg[2])
    if isinstance(arg, date):
        return (arg.year, arg.month, arg.day)

def make_year(y):
    if y < 100:
        if y > 49:
            y += 1900
        else:
            y += 2000
    return y

def chance_not_expired(expiry, today=None):
    today = today or date.today()
    if not isinstance(today, date):
        (y, m, d) = get_date_tuple(today)
        y = make_year(y)
        today = date(y, m, d)
    (n1, n2, n3) = get_date_tuple(expiry)
    dates = [(n1, n2, n3), (n3, n1, n2), (n3, n2, n1)]
    valid_dates = 0
    still_good = 0
    for i in range(0, 3):
        (y, m, d) = dates[i]
        y = make_year(y)
        try:
            expiry = date(y, m, d)
            valid_dates += 1
            if not today > expiry:
                still_good += 1
        except:
            pass
    if valid_dates > 0:
        return int(100.0 * still_good / valid_dates + .5)
    return 0

if __name__ == '__main__':
    pass
