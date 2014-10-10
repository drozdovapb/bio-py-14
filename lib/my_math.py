def max(a,b):
    """ (number, number) -> number
    returns the larger of two numbers

    >>> max(1,2)
    2
    >>> max(2/2, 1.00)
    1.0
    """
    if a > b:
        return a
    return b

def min(a,b):
    """ (number, number) -> number
    returns the smaller of two numbers
    >>> min(1,2)
    1
    >>> min(2/2, 1.00)
    1.0
    """
    if a < b:
        return a
    return b

def ceil(a):
    """ (float) -> (int)
    returns the closest integer greater or equal a
    >>> ceil(4.9)
    5
    >>> ceil(14.1)
    15
    >>> ceil(-4.9)
    -4
    """
    if a - int(a) <= 0:
        return float(int(a))
    return int(a + 1.0)

def floor(a):
    """ (float) -> (int)
    returns the closest integer less or equal a
    >>> floor(15.1)
    15
    >>> floor(3.9)
    3
    >>> floor(-4.9)
    -5
    """
    if a - int(a) >= 0:
        return int(a)
    return int(a - 1.0)
