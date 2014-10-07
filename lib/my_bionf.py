#! /usr/bin/env python

def is_dna(string):
    ''' (string) -> (bool)
    This function checks whether a string is a valid DNA sequence
    >>> is_dna('atgc')
    True
    >>> is_dna('aug')
    False
    '''
    string = string.upper()
    counter=0
    for n in range(0, len(string)):
        counter = counter + (string[n]!='A' and string[n]!='C' and string[n]!='G' and string[n]!='T')
    return not(bool(counter))

def is_stop_codon(codon):
    ''' (string) -> (bool)
    This function check whether a string is a stop codon
    >>>
    '''

    codon = codon.upper()
    if codon=='UAA' or codon=='UAG' or codon=='UGA' or codon=='TAA' or codon=='TAG' or codon=='TGA':
        return True
    return False
    
