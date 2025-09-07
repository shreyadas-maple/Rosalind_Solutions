from itertools import product

def kmers_Lexi (file):
    # Read in the file with the symbols and the length of n
    data = open(file).read().replace('\n', ' ').split(" ")

    # Symbols are in the list of data except the last item
    symbols = data[:-2]
    # The last item in the data list is the n length
    n_len = int(data[-2])

    # Create a list with all the permutations 
    partial_perms = product(symbols, repeat=n_len)
    
    # Create an output file
    with open("lexf_ans.txt", 'w') as file:
        # Format the print of the combos according to instructions
        for perms in partial_perms:
            line = ""
            for set in perms:
                line += set
            line += "\n"
            file.write(line)

kmers_Lexi("rosalind_lexf.txt")