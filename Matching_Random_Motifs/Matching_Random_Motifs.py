def matching_random_motif(file):
    #
    # This function calculates the probability of get a match of the motif given
    # with a certain gc content.
    # Input: File with the number of random string, gc content percentage, and
    # the motif to match
    # Output: A file with the probability calculated
    #

    # Get the number of random strings, gc content, and motif from the fils
    N, gc, motif = open(file).read().replace("\n", " ").split(" ")

    # Convert the gc content to a float
    gc = float(gc)

    # Calculate the probability of each nucleotide using the gc content
    P_C = gc/2
    P_G = gc/2
    P_A = (1 - gc)/2
    P_T = P_A

    # Initialize the variable to hold the total probability of the motif
    p_tot = 1

    # Calculate the probability of creating the motif given
    for nt in motif:
        # If the nucleotide is a C, multiply the probability for a C
        if nt == "C":
            p_tot *= P_C
        # If the nucleotide is a G, multiply the probability for a G
        elif nt == "G":
            p_tot *= P_G
        # If the nucleotide is a A, multiply the probability for a A
        elif nt == "A":
            p_tot *= P_A
        # Else the nucleotide is a T, multiply the porbability for a T
        else:
            p_tot *= P_T

    # Calculate the probability of not finding 1 match to the motif
    no_match = 1 - p_tot

    # Calculate the probability of not finding N number of matches
    N_no_match = no_match ** int(N)

    # Calculate the probability of finding at least one match, which is the complement of the N_no_match
    prob = 1 - N_no_match

    # Write a file with the calculated probability rounded to 3 decimal points
    with open("rstr_ans.txt", "w") as f:
        prob = round(prob, 3)
        f.write(str(prob))

# Function call with the input file
matching_random_motif("rosalind_rstr.txt")