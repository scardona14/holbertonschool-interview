#!/usr/bin/python3

"""
Script that reads stdin line by line and computes metrics.

The script tracks:
- Total file size from log entries.
- The number of occurrences of specific HTTP status codes.
After every 10 lines or on a keyboard interruption (CTRL + C),
it prints the metrics gathered so far.
"""

import sys


def printsts(dic, size):
    """ Prints the current statistics of total file size and status codes """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


# Initialize the status codes and counters
sts = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}
count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printsts(sts, size)

        stlist = line.split()
        count += 1

        # Update the file size
        try:
            size += int(stlist[-1])
        except (ValueError, IndexError):
            pass

        # Update the status code count if valid
        try:
            if stlist[-2] in sts:
                sts[stlist[-2]] += 1
        except IndexError:
            pass

    # Print the final stats at the end of the input
    printsts(sts, size)

except KeyboardInterrupt:
    # Handle keyboard interrupt and print final stats
    printsts(sts, size)
    raise