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
        if base in ALLOWED_NUC:
            transcribed += TRANSCRIPTION_MAPPING[base]
        else:
            print('A non-allowed nucleotide is present in the sequence.')
            return #return nothing if an incorrect nucleotide is present
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
            print('A non-allowed nucleotide is present in the sequence.')
            return
    #Now we return the reverse of the transcribed sequence
    return transcribed[::-1]