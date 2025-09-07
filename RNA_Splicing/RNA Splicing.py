
def introns_seq(FASTA_file):
    ## Open the FASTA file and parse through the sequences, separating the DNA sequence from the introns
    file = open(FASTA_file, "r").read().replace("\n", "").split(">Rosalind_")
    new_file = file[2:]
    dna_str = str(file[1:2])
    introns = []

    for seq in new_file:
        introns.append(str(seq[4:]))

    ## We want to find where the introns are located in the DNA string
    ## Then we will take out the introns from this DNA string
    for intron in introns:
        dna_str = dna_str.replace(intron, "")

    length = len(dna_str)
    return dna_str [6:length-2]

def transcribe(dna_string):
    dna_string = dna_string.upper()
    rna_string = ''

    for i in range(len(dna_string)):
        if dna_string[i] == 'T':
            rna_string += 'U'
        else:
            rna_string += dna_string[i]

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
        else:
            return protein_str
    return protein_str

string = translate(transcribe(introns_seq("rosalind_splc.txt")))

# Create an output file with the pairs
with open("splc_answer.txt", 'w') as file:
    file.write(string)