#!/usr/bin/python3
import hidden_4 as h
if __name__ == "__main__":
    for n in dir(h):
        if n[:2] != "__":
            print("{:s}".format(n))
