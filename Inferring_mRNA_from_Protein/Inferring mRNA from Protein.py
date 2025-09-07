def reversetranslate(pro_file):
    pro_str = open(pro_file).read().upper()
    num_rna = 3
    m = 1000000

    for i in range(0, len(pro_str)):
        if pro_str[i] == 'A':
            num_rna = (num_rna * 4) % m
        elif pro_str[i] == 'G':
            num_rna = (num_rna * 4) % m
        elif pro_str[i] == 'R':
            num_rna = (num_rna * 6) % m
        elif pro_str[i] == 'N':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'D':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'C':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'E':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'Q':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'H':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'I':
            num_rna = (num_rna * 3) % m
        elif pro_str[i] == 'L':
            num_rna = (num_rna * 6) % m
        elif pro_str[i] == 'K':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'F':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'P':
            num_rna = (num_rna * 4) % m
        elif pro_str[i] == 'S':
            num_rna = (num_rna * 6) % m
        elif pro_str[i] == 'T':
            num_rna = (num_rna * 4) % m
        elif pro_str[i] == 'W':
            num_rna = (num_rna * 1) % m
        elif pro_str[i] == 'Y':
            num_rna = (num_rna * 2) % m
        elif pro_str[i] == 'V':
            num_rna = (num_rna * 4) % m
        elif pro_str[i] == 'M':
            num_rna = (num_rna * 1) % m
        else:
            num_rna = num_rna
    
    # Create an output file
    with open("mrna_ans.txt", 'w') as file:
        file.write(str(num_rna))


reversetranslate('rosalind_mrna.txt')
