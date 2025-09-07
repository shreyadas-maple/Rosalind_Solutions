
def complement(DNA):
    # This is a function that writes the complement of a provided DNA sequence
    comp = ""
    for i in DNA:
        if i == "T":
            comp += "A"
        elif i == "C":
            comp += "G"
        elif i == "G":
            comp += "C"
        else:
            comp += "T"
    # Return the complement to the function call
    return comp

def revpalin (dna_file):
    # Read-in the data file with the Sequence ID and DNA sequence
    data = open(dna_file).read().replace('\n', '').split(">Rosalind_")

    # Get only the DNA sequence
    DNA = data[1][4:]

    # Intialize variable to store the position number and length of the reverse palindrome
    pos = []
    lens = []

    # These are the lengths allowed for the palindromes: 4-12
    lengths = range(4, 13)

    # Loop through the entire sequence
    for i in range(len(DNA)):
        # Loop through the lengths allowed
        for j in lengths:
            # Check if the position plus the length is within the length of the DNA,
            # This prevents out of bounds error
            if i + j <= len(DNA):
                # Temp variable to store the sliced string from the sequence to be analyzed
                temp = DNA[i: i + j]
                # Get the complement of the sequence sliced
                com = complement(temp)
                # Reverse the complement to get finally the reverse complement to be analyzed
                flip = com[::-1]
                # Check if the original sequence sliced and the reverse complement are the same
                if temp == flip:
                    # Append the position and length if the sequences are equal
                    pos.append(i+1)
                    lens.append(j)

    # Create an output file
    with open("revp_ans.txt", 'w') as file:   
        for i in range(len(pos)):
            file.write(str(pos[i]))
            file.write(" ")
            file.write(str(lens[i]))
            file.write("\n")
    
revpalin("rosalind_revp.txt")