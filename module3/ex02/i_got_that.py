#!/usr/bin/env python3

i = 1

print("What you gotta say? : ", end = "")

while i > 0:
    text = input()
    if text == "STOP":
        break
    print(f"I got that! Anything else? : ", end = "")
    i += 1
