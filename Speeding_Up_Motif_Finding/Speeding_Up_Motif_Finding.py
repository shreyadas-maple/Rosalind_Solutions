def LPS(file):
    # Read in the file from the directory
    data = open(file).read().replace("\n", " ").split(" ")

    # The sequence is the second item onwards in the data array
    sequence = "".join(data[1:])

    #print(sequence)

    # Populate the first item in the failure array with 0
    lps = [0]

    # This keep track of how long the longest substring is
    length = 0

    # This is what we use to traverse through the sequence
    i = 1

    # Continue the loop until the last letter in the sequence
    while i < len(sequence):
        # Case 1: the suffix and prefix match
        if sequence[i] == sequence[length]:
            # Incrase the length by 1 
            length += 1
            # Append the length value to the failure_array
            lps.append(length)
            # Move to the next letter in teh sequence
            i += 1
        # Case 2: the suffix and prefix don't match and length is not 0. 
        # This means that there might be a subsequence before sequence[i]
        elif sequence[i] != sequence[length] and length != 0:
            length = lps[length - 1]
        else:
            length = 0
            lps.append(0)
            i += 1

    with open("kmp_answer.txt", 'w') as file:
        string = ""
        for l in lps:
            string += str(l) + " "
        file.write(string)

LPS("rosalind_kmp.txt")