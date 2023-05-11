#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 1
    argv_len = len(argv) - 1
    if len(argv) == 1:
        print("{:d} arguments.".format(argv_len))
    elif len(argv) == 2:
        print("{:d} argument:".format(argv_len))
        print("{:d}: {:s}".format(i, argv[i]))

    else:
        print("{:d} arguments:".format(argv_len))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))

