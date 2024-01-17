# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    transcribed = '' #To be filled in with the transcibed sequence
    for base in seq:
        # Test if a given base is allowed, and add its pair to transcribed if so
        if base in ALLOWED_NUC:
            transcribed += TRANSCRIPTION_MAPPING[base]
        else:
            #if base not in allowed nucleotide, report the base and raise value error
            raise ValueError('Non-allowed nucleotide \'' + base + '\' encountered.')
    return transcribed

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    transcribed = '' #To be filled in with the transcibed sequence
    for base in seq:
        if base in ALLOWED_NUC:
            transcribed += TRANSCRIPTION_MAPPING[base]
        else:
            raise ValueError('Non-allowed nucleotide \'' + base + '\' encountered.')
    #Now we return the reverse of the transcribed sequence
    return transcribed[::-1]