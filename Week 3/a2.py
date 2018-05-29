def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

    
def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide) 


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence dna contains no characters other than 'A', 'T', 'C', 'G'

    >>> is_valid_sequence('')
    True
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('G')
    True
    >>> is_valid_sequence('TT')
    True
    >>> is_valid_sequence('AB')
    False
    >>> is_valid_sequence('AA')
    True
    >>> is_valid_sequence('ATCGGC3')
    False

    '''

    return all(char in 'ATCG' for char in dna)

def insert_sequence(dna1, dna2, pos):
    ''' (str, str, int) -> str

    Return the DNA sequence obtained by inserting the DNA sequence dna2 into the DNA sequence dna1 at the given index pos.

    >>> insert_sequence('', '', 0)
    ''
    >>> insert_sequence('TTCG', 'AA', 4)
    'TTCGAA'
    >>> insert_sequence('TTCG', 'AA', 2)
    'TTAACG'
    >>> insert_sequence('TTCG', 'AA', 0)
    'AATTCG'
    >>> insert_sequence('', 'ATA', 0)
    'ATA'
    >>> insert_sequence('ATA', '', 2)
    'ATA'
    '''

    return dna1[:pos] + dna2 + dna1[pos:]

def get_complement(nucleotide):
    '''(str) -> str

    Returns the complement of the entered nucleotide

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    '''

    return {'A':'T','T':'A','C':'G','G':'C'}[nucleotide]

def get_complementary_sequence(dna):
    '''(str) -> str

    Return the dna sequence that is complementary to the given DNA sequence

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('CG')
    'GC'
    '''
    result = ""
    for char in dna:
        result += get_complement(char)
    return result
