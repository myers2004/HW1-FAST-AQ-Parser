# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    #testing a DNA sequence with allowed nucleotides
    test_seq = 'ACTGAACCC'
    test_out = 'UGACUUGGG'
    assert transcribe(test_seq) == test_out

    #testing a DNA sequence with allowed nucleotides
    test_seq_error = 'ACYGAACCC'
    test_error_out = 'A non-allowed nucleotide is present in the sequence.'
    assert transcribe(test_seq_error) == test_error_out
    
    #testing an empty sequence
    assert transcribe('') == ''


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    #testing a DNA sequence with allowed nucleotides
    test_seq = 'ACTGAACCC'
    test_out = 'GGGUUCAGU'
    assert transcribe(test_seq) == test_out

    #testing a DNA sequence with allowed nucleotides
    test_seq_error = 'ACYGAACCC'
    test_error_out = 'A non-allowed nucleotide is present in the sequence.'
    assert transcribe(test_seq_error) == test_error_out
    
    #testing an empty sequence
    assert transcribe('') == ''