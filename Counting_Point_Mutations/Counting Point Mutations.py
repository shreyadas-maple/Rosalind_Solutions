
def hamming_dist(dna_file):
    strings = list(open(dna_file).read().replace('\n', ' ').split(" "))
    str1 = strings[0].upper()
    str2 = strings[1].upper()
    num_diff = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            num_diff += 1
        else:
            num_diff += 0

    # Create an output file with counts
    with open("hamm_ans.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(num_diff))

hamming_dist("rosalind_hamm.txt")