#!/usr/bin/env python
import os
import sys
import getopt

_filename = ''
_verbose = False

# Show program usage message (always exits)
def show_usage():
    print "\nUSAGE: " + sys.argv[0] + " [options] filename"
    print "  filename = input file to use"
    print "OPTIONS:"
    print "  -?, -h, --help = show this usage screen"
    print "  -v = verbose (show heading and footer in output)"
    sys.exit(0)

# Process command-line arguments
def process_cmd_args():
    global _filename
    global _verbose
    try:
        opts,args = getopt.getopt(sys.argv[1:], '?hv', ['help', 'verbose'])
    except getopt.GetoptError:
        show_usage()

    if len(args) < 1:
        show_usage()

    for opt,arg in opts:
        if opt in ("-?","-h","--help"):
            show_usage()
        elif opt in ("-v","--verbose"):
            _verbose = True

    for arg in args:
        _filename = arg
    if not os.path.isfile(_filename):
        print "\nInput file not found"
        sys.exit(1)

# Process input line
def process_line(line):
    unique_chars = []
    digits = []
    for ch in line:
        if ch == '\n':
            break;
        if unique_chars.count(ch) == 0:
            unique_chars.append(ch)
        digit = unique_chars.index(ch)
        if digit < 2:
            digit = 1 - digit;
        digits.insert(0, digit)
    base = len(unique_chars)
    if base < 2:
        base = 2
    result = 0L
    for i in xrange(len(digits)):
        result += long(digits[i] * pow(base, i))
    return str(result)

# Main Program
process_cmd_args()

file = open(_filename)

total = file.readline()
if _verbose:
    print "\nTotal cases should be: " + str(total)

case_count = 0;
for line in file:
    case_count += 1
    print "Case #" + str(case_count) + ": " + process_line(line)

if _verbose:
    print "\nEND OF OUTPUT"

file.close()
