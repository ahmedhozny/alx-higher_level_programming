#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{:c}".format((i + 97) if i % 2 == 1 else (i + 65)), end="")
