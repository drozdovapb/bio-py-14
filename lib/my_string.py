def startswith(string, begin):
    """ (string, string) -> (bool)
    Defines whether a string begins with some substring
    >>> startswith('an extremely long test string', 'an')
    True
    >>> startswith('an extremely long test string', 'string')
    False
    """
    return string[:len(begin)] == begin

def endswith(string, end):
    """ (string, string) -> (bool)
    Defines whether a string ends with some substring
    >>> endswith('an extremely long test string', 'an')
    False
    >>> endswith('an extremely long test string', 'string')
    True
    """
    return string[-len(end):] == end

def isdigit(s):
    """ (string) -> (bool)
    Defines whether a one-letter string is in fact a digit
    >>> isdigit('4')
    True
    >>> isdigit('a')
    False
    """
    return (s >= '0' and s <= '9')
