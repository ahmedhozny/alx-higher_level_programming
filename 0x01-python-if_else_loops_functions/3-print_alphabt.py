#!/usr/bin/python3
for i in range(97, 123):
    if f"{i:c}" != 'e' and f"{i:c}" != 'q':
        print("{:c}".format(i), end="")
