#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    phrase = sys.argv[2]
    keyword = sys.argv[1]

    scan = re.findall(keyword, phrase, re.I) # IGNORECASE
    #print(scan) # displays repeated keywords

    if len(scan) == 0:
        print("none")
    else:
        print(len(scan))
