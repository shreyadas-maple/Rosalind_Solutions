import numpy as np

## We need a function that will transcribe the DNA string into RNA
## we have coded this before

def transcribe(dna_string):
    ## Make the DNA string into all upper case
    dna_string = dna_string.upper()
    ## This is where we will store the transcribed RNA and return at the end of the function
    rna_string = ''

    ## Iterate through the DNA string and change the Ts to Us
    for i in range(len(dna_string)):
        if dna_string[i] == 'T':
            rna_string += 'U'
        else:
            rna_string += dna_string[i]

    ## Return the transcribed RNA string
    return rna_string

def translate(rna_str):
    rna_str = rna_str.upper()
    protein_str = ''

    for i in range(0, len(rna_str), 3):
        if rna_str[i: i +3] == "UUU" or rna_str[i: i +3] == "UUC":
            protein_str += "F"
        elif rna_str[i: i +3] == "UUA" or rna_str[i: i +3] == "UUG":
            protein_str += "L"
        elif rna_str[i: i +3] == "UCU" or rna_str[i: i +3] == "UCC" or rna_str[i: i +3] == "UCA" or rna_str[i: i +3] == "UCG":
            protein_str += "S"
        elif rna_str[i: i +3] == "UAU" or rna_str[i: i +3] == "UAC":
            protein_str += "Y"
        elif rna_str[i: i +3] == "UGU" or rna_str[i: i + 3] == "UGC":
            protein_str += "C"
        elif rna_str[i: i +3] == "UGG":
            protein_str += "W"
        elif rna_str[i: i +3] == "CUU" or rna_str[i: i + 3] == "CUC" or rna_str[i: i + 3] == "CUA" or rna_str[i: i + 3] == "CUG":
            protein_str += "L"
        elif rna_str[i: i +3] == "CCU" or rna_str[i: i + 3] == "CCC" or rna_str[i: i + 3] == "CCA" or rna_str[i: i + 3] == "CCG":
            protein_str += "P"
        elif rna_str[i: i +3] == "CAU" or rna_str[i: i + 3] == "CAC":
            protein_str += "H"
        elif rna_str[i: i +3] == "CAA" or rna_str[i: i + 3] == "CAG":
            protein_str += "Q"
        elif rna_str[i: i +3] == "CGU" or rna_str[i: i + 3] == "CGC" or rna_str[i: i + 3] == "CGG" or rna_str[i: i + 3] == "CGA":
            protein_str += "R"
        elif rna_str[i: i +3] == "AUU" or rna_str[i: i + 3] == "AUC" or rna_str[i: i + 3] == "AUA":
            protein_str += "I"
        elif rna_str[i: i +3] == "AUG":
            protein_str += "M"
        elif rna_str[i: i +3] == "ACU" or rna_str[i: i + 3] == "ACC" or rna_str[i: i + 3] == "ACA" or rna_str[i: i + 3] == "ACG":
            protein_str += "T"
        elif rna_str[i: i +3] == "AAU" or rna_str[i: i + 3] == "AAC":
            protein_str += "N"
        elif rna_str[i: i +3] == "AAA" or rna_str[i: i + 3] == "AAG":
            protein_str += "K"
        elif rna_str[i: i +3] == "AGU" or rna_str[i: i + 3] == "AGC":
            protein_str += "S"
        elif rna_str[i: i +3] == "AGA" or rna_str[i: i + 3] == "AGG":
            protein_str += "R"
        elif rna_str[i: i +3] == "GUU" or rna_str[i: i + 3] == "GUC" or rna_str[i: i + 3] == "GUA" or rna_str[i: i + 3] == "GUG":
            protein_str += "V"
        elif rna_str[i: i +3] == "GCU" or rna_str[i: i + 3] == "GCA" or rna_str[i: i + 3] == "GCC" or rna_str[i: i + 3] == "GCG":
            protein_str += "A"
        elif rna_str[i: i +3] == "GAU" or rna_str[i: i + 3] == "GAC":
            protein_str += "D"
        elif rna_str[i: i +3] == "GAA" or rna_str[i: i + 3] == "GAG":
            protein_str += "E"
        elif rna_str[i: i +3] == "GGU" or rna_str[i: i + 3] == "GGC" or rna_str[i: i + 3] == "GGG" or rna_str[i: i + 3] == "GGA":
            protein_str += "G"
        elif rna_str[i: i +3] == "UAG" or rna_str[i: i + 3] == "UGA" or rna_str[i: i + 3] == "UAA":
            protein_str += "Z"
            break
        else:
            return protein_str
    return protein_str

def findStart(DNAstring):

    for i in DNAstring:
        if 'ATG' in DNAstring:
            return i
        else:
            break

def findSTOP(DNAstring):
    for i in range(len(DNAstring)):
        if DNAstring[i:i+3] == 'TAG' or DNAstring[i:i+3] == 'TGA' or DNAstring[i:i+3] == 'TAA':
            return i
        else:
            break
def complement(dna_str):
    dna_str = dna_str
    complement_str= ""

    for i in range(len(dna_str)):
        if dna_str[i] == 'A':
            complement_str += 'T'
        elif dna_str[i] == 'T':
            complement_str += 'A'
        elif dna_str[i] == 'G':
            complement_str += 'C'
        elif dna_str[i] == 'C':
            complement_str += 'G'
        else:
            return 'Error'

    return complement_str[::-1]

def proteinString(fastaFile):
    ## Open the fasta file and remove the ID from the file
    data = open(fastaFile).read().replace('\n', '').replace('>Rosalind_', '')
    ## Store the DNA sequence by itself
    DNA = data[4:]
    ## The complement DNA sequence
    complementDNA = complement(DNA)

    prot = []

    for i in range(len(DNA)):
        if DNA[i:i+3] == "ATG":
            seq = translate(transcribe(DNA[i:]))
            if seq.find("Z") != -1:
                prot.append(seq[:-1])
        else:
            i += 1
    for i in range(len(complementDNA)):
        if complementDNA[i:i+3] == "ATG":
            seq = translate(transcribe(complementDNA[i:]))
            if seq.find("Z") != -1:
                prot.append(seq[:-1])
        else:
            i += 1

    final_prot = np.unique(prot)

    # Create an output file with the pairs
    with open("orf_answer.txt", 'w') as file:
        for i in final_prot:
            file.write(i)
            file.write("\n")

proteinString('rosalind_orf.txt')