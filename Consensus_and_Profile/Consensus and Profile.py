def parseFASTA(fastaFile):
    ## Save all the sequences in a separate array
    seq_list = []

    ## Open the file and replacing all the newlines and split the data where a new sequence starts
    data = open(fastaFile).read().replace('\n', '').split(">")
    newdata = data[1:]

    for i in range(0, len(newdata)):
        if newdata[i].startswith("Rosalind"):
            seq_list.append(newdata[i][13:])

    ## Since we are only going to use the sequence array, return the sequence array only
    return seq_list


def consensus(fastaFile):
    # Parse through the file with the sequences
    seq_list = parseFASTA(fastaFile)

    # Get the number of sequences that we must loop through
    n = len(seq_list)

    # Make a dictionary to store the number of bases from each sequence 
    bases = {
        "A": [],
        "C": [],
        "G": [],
        "T": []
    }

    # This dictionary will be used later to figure out the consensus sequence
    indices = {
        0 : "A",
        1 : "C",
        2 : "G",
        3 : "T"
    }

    # Create the string variable to store the consensus sequence
    con_seq = ""

    # Loop through the length of each sequence
    for i in range(len(seq_list[0])):
        # We set the number of bases for each nucleotide to 0 at the beginning of 
        # each loop iteration
        A = 0
        C = 0
        G = 0
        T = 0
        # We loop through each sequence and count the number of each base
        for j in range(n):
            if seq_list[j][i] == "A":
                A += 1
            elif seq_list[j][i] == "C":
                C += 1
            elif seq_list[j][i] == "G":
                G += 1
            else:
                T += 1
        # Append the number of nucleotides to the corresponding dictionary key
        bases["A"].append(A)
        bases["C"].append(C)
        bases["G"].append(G)
        bases["T"].append(T)

    # Figuring out the consensus sequence
    # We loop through the length of a sequence
    for idx in range(len(seq_list[0])):
        # For each base, we get the number of each nucleotide
        nums = [bases["A"][idx], bases["C"][idx], bases["G"][idx], bases["T"][idx]]

        # We get the value that is the max in the list of nums
        max_num = max(nums)

        # We get the "key" (nucleotide) that corresponds to this max value and append
        # to the consensus sequence string
        con_seq += indices[nums.index(max_num)]
    
    # Save the consensus sequence to a file and the matrix to finding the consensus sequence
    with open("cons_ans.txt", 'w') as file:
        file.write(con_seq)
        file.write("\n")
        for key, value in bases.items():
            file.write(f"{key}: ")
            for val in value:
                string = str(val) + " "
                file.write(string)
            file.write("\n")

consensus("rosalind_cons.txt")

