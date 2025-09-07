import math

def probSeq(seq, prob_A, prob_T, prob_C, prob_G):

    # Initialize the variable with probability
    n = 1

    # Multiply the probabilities according to the nucleotide
    for i in seq:
        if i == "A":
            n *= prob_A
        elif i == "T":
            n *= prob_T
        elif i == "C":
            n *= prob_C
        elif i == "G":
            n *= prob_G
        else:
            return "Invalid character"
    # Return the sequence probability
    return n

def randStrings(file):
    # Read the file to get sequence and probabilities
    data = open(file).read().replace("\n", " ").split(" ")

    # Get the sequence as the data's first item
    sequence = data.pop(0)

    # Remove the last item because it was " "
    data.pop(-1)

    # Initialize the list to contain the GC content frequencies
    GC_content = []

    # Append the GC content frequencies 
    for i in data:
        GC_content.append(float(i))

    # Initialize the list to contain the logs
    logs = []

    # Calculate the frequencies using the GC content frequencies in the list
    for i in GC_content:
        prob_C = i / 2
        prob_G = prob_C
        prob_A = (1 - i) / 2
        prob_T = prob_A

        # Calculate the probability for that sequence
        prob_seq = probSeq(sequence, prob_A, prob_T, prob_C, prob_G)

        # Append the log of that probability, rounded to 3 places
        logs.append(round(math.log10(prob_seq), 3))

    # Create an output file
    with open("prob_ans.txt", 'w') as file:
        for i in logs:
            string = str(i) + " "
            file.write(string)

randStrings("rosalind_prob.txt")
