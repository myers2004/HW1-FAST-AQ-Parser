# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    #test a blank fasta file
    blankfasta = FastaParser('tests/blank.fa')
    with pytest.raises(ValueError):
        for seq in blankfasta:
            pass
    
    #test a bad fasta file
    badfasta = FastaParser('tests/bad.fa')
    with pytest.raises(ValueError):
        for seq in badfasta:
            pass
    
    #test the good fasta file
    test_fasta = FastaParser('data/test.fa')
    for seq in test_fasta:
        assert seq[0].startswith('seq')



def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fastq_data = FastaParser('data/test.fq')
    for seq in fastq_data:
        assert seq[0] == None
        break
    fasta_data = FastaParser('data/test.fa')
    for seq in fasta_data:
        assert seq[0] != None
        break


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    test_fastq = FastqParser('data/test.fq')
    for seq in test_fastq:
        assert seq[0].startswith('seq')

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    fastq_data = FastqParser('data/test.fq')
    for seq in fastq_data:
        assert seq[0] != None
        break
    fasta_data = FastqParser('data/test.fa')
    for seq in fasta_data:
        assert seq[0] == None
        break