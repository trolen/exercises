#!/usr/bin/env python
def hey(input_string):
    if input_string.strip() == '':
        return 'Fine. Be that way!'
    if input_string.isupper():
        return 'Woah, chill out!'
    if input_string[-1] == '?':
        return 'Sure.'
    return 'Whatever.'
