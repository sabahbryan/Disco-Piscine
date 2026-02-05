#!/usr/bin/env python3

import sys

#print(sys.argv)
#print(list(reversed(sys.argv)))

# start at '1' to ignore "parameters.py" when "print()"
# use '-1' to ignore "parameters.py" when reversing
#i = 1
j = len(sys.argv) - 1

if len(sys.argv) <= 2:
    print("none")
else:
    #while i < len(sys.argv):
    #    i += 1
    while j > 0:
        print(sys.argv[j])
        j -= 1
