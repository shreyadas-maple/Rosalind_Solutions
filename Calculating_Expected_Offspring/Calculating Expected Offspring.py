
def expected_offspring(offspring_file):

    num = list(open(offspring_file).read().replace('\n', ' ').split(" "))

    AA_AA_off = int(num[0]) * 2
    AA_Aa_off = int(num[1]) * 2
    AA_aa_off = int(num[2]) * 2
    Aa_Aa_off = int(num[3]) * ((1+2)/2)
    Aa_aa_off = int(num[4]) * ((0+2)/2)
    aa_aa_off = int(num[5]) * 0

    sum = AA_AA_off + AA_Aa_off + AA_aa_off + Aa_Aa_off + Aa_aa_off + aa_aa_off

    # Create an output file with counts
    with open("iev_ans.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(sum))

expected_offspring("rosalind_iev.txt")