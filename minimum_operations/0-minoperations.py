#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the minimum number of operations needed to get exactly n 'H' characters in the file.

    Parameters:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The minimum number of operations required to achieve exactly n 'H' characters.
         Returns 0 if n is impossible to achieve.
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
