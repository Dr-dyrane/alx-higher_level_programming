#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    for i in range(1, len(argv)):
        total = total + int(argv[i])
    print("{:d}".format(total))

