def complement_dna(dna_file):
    dna_str = str(open(dna_file).read().upper())
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
            print('Error')

    # Create an output file with counts
    with open("complement_a_strand_of_dna.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(complement_str))


complement_dna('rosalind_revc.txt')