def is_dna(string):
    """ (string) -> (bool)
    This function checks whether a string is a valid DNA sequence
    >>> is_dna('atgc')
    True
    >>> is_dna('aug')
    False
    """
    string = string.upper()
    counter=0
    for n in range(0, len(string)):
        counter = counter + ((string[n] != 'A') \
                             and (string[n] != 'C') \
                             and (string[n] != 'G') \
                             and (string[n] != 'T'))
        if counter:
            return False
    return True

def is_stop_codon(codon):
    """ (string) -> (bool)
    This function check whether a string is a stop codon
    >>> is_stop_codon('UGA')
    True
    >>> is_stop_codon('AUG')
    False
    """
    codon = codon.upper()
    return (codon == 'UAA') or (codon == 'TAA') \
       or (codon == 'UAG') or (codon == 'TAG') \
       or (codon == 'UGA') or (codon == 'TGA')
