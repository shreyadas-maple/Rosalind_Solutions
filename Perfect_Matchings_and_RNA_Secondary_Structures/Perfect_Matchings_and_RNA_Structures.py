import math


def countNucleotides (sequence):
    A_counts = 0
    C_counts = 0
    U_counts = 0
    G_counts = 0

    for i in sequence:
        if i == "A":
            A_counts += 1
        elif i == "C":
            C_counts += 1
        elif i == "U":
            U_counts += 1
        elif i == "G":
            G_counts += 1
        else:
            return "Invalid character"
        
    return [A_counts, U_counts, C_counts, G_counts]

def perfectMatch (file):
    data = open(file).read().replace("\n", "")

    sequence = data[14:]

    A_counts, U_counts, C_counts, G_counts = countNucleotides(sequence)

    # Check that #A = #U and #C = #G
    if A_counts != U_counts:
        return "Error: no perfect matchings because # of A and U are not equal"
    if C_counts != G_counts:
        return "Error: no perfect matchings because # of C and G are not equal"
    
    # Create an output file with the pairs
    with open("pmch_answer.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(math.factorial(A_counts) * math.factorial(C_counts)))

perfectMatch("rosalind_pmch.txt")