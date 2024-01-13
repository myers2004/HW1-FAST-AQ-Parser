from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    # Create instance of FastqParser
    fastaData = FastaParser('data/test.fa')
    fastqData = FastqParser('data/test.fq')
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    for seq in fastaData:
       print(transcribe(seq[1]))
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    for seq in fastqData:
        print(transcribe(seq[1]))


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    for seq in fastaData:
       print(reverse_transcribe(seq[1]))
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    for seq in fastqData:
        print(reverse_transcribe(seq[1]))


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
