#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    print("{} argument{}{}".format(
        l,
        "" if l == 1 else "s",
        ":" if l != 0 else "."
    ))
    for i in range(1, l + 1):
        print("{}: {}".format(i, sys.argv[i]))
