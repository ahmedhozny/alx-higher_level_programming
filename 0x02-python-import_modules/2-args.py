#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv) - 1
    print("{} argument{}".format(length, "" if length == 1 else "s"), end="")
    print("{}".format(":" if length else "."))
    for i in range(1, length + 1):
        print("{}: {}".format(i, sys.argv[i]))
