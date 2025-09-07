
def transcribe(dna_file):
    dna_string = open(dna_file).read().upper()
    rna_string = ''

    for i in range(len(dna_string)):
        if dna_string[i] == 'T':
            rna_string += 'U'
        else:
            rna_string += dna_string[i]

    # Create an output file with counts
    with open("transcribing_dna_into_rna.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(rna_string))

transcribe('rosalind_rna.txt')