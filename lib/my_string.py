#! /usr/bin/env python

def startswith(string, begin):
    ''' (string, string) -> (bool)
    Defines whether a string begins with some substring
    >>> startswith('an extremely long test string', 'an')
    True
    >>> startswith('an extremely long test string', 'string')
    False
    '''
    if string[:len(begin)] == begin:
        return True
    return False

def endswith(string, end):
    ''' (string, string) -> (bool)
    Defines whether a string ends with some substring
    >>> endswith('an extremely long test string', 'an')
    False
    >>> endswith('an extremely long test string', 'string')
    True
    '''
    if string[-len(end):] == end:
        return True
    return False

def isdigit(s):
    ''' (string) -> (bool)
    Defines whether a one-letter string is in fact a digit
    >>> isdigit('4')
    True
    >>> isdigit('a')
    False
    '''
    if s < 'a':
        return True
    return False
