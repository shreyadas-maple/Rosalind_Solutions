
def find_motif(dna_file):
    strings = list(open(dna_file).read().replace('\n', ' ').split(" "))
    str1 = strings[0].upper()
    str2 = strings[1].upper()
    str2_len = len(str2)
    positions = ''

    for i in range(len(str1)):
        if str1[i: i + str2_len] == str2:
            positions += str(i + 1) + " "
        else:
            positions += ''

    # Create an output file with counts
    with open("subs_ans.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(positions))


find_motif("rosalind_subs.txt")
