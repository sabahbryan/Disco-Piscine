#!/usr/bin/env python3

import sys

#print(sys.argv)

# start at '1' to ignore "parameters.py"
i = 1

while i < len(sys.argv):
    #print(sys.argv[i])
    i += 1

print("Number of parameters:", len(sys.argv) - 1)
