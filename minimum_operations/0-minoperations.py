#!/usr/bin/python3

def minOperations(n):
    """
    Function that returns the minimun operations to get n
    """
    if not isinstance(n, int):
        return 0
    
    op = 0
    i = 2
    while (i <= n):
        if not (n % i):
            op += i
            i = i
        i += 1
    return op
