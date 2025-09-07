
def countDNA(dna_file):
    dna_str = open(dna_file).read()
    num_A = []
    num_C = []
    num_G = []
    num_T = []

    for i in range(len(dna_str)):
        if dna_str[i] == "A":
            num_A.append(dna_str[i])
        elif dna_str[i] == "C":
            num_C.append(dna_str[i])
        elif dna_str[i] == 'G':
            num_G.append(dna_str[i])
        elif dna_str[i] == 'T':
            num_T.append(dna_str[i])
        else:
            print('Error')
    
    # Create an output file with counts
    with open("counting_dna_nucleotides.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(len(num_A)) + " " + str(len(num_C)) + " " + str(len(num_G)) + " " + str(len(num_T)))

countDNA("rosalind_dna.txt")
