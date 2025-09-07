def parseFASTA(fastaFile):
    # Save all the sequences in a separate list
    seq_list = []

    # Save all the sequence IDs in a separate list
    ids_list = []

    # Open the file and replacing all the newlines and split the data where a new sequence starts
    data = open(fastaFile).read().replace('\n', '').split(">")
    newdata = data[1:]

    # Based on when Rosalind appears in the array of data, we append the sequences and IDs to the
    # respective lists
    for i in range(0, len(newdata)):
        seq_list.append(newdata[i][13:])
        ids_list.append(newdata[i][0:13])

    # Return the sequence and IDs list
    return seq_list, ids_list

def overlap_graphs(fastaFile):
    seq_list, ids_list = parseFASTA(fastaFile)

    # We will use the index values to denote which sequences are pairs
    pairs = []

    # We have to compare the first 3 of 1 sequence to the last 3 of another sequence
    for i in range(len(seq_list)):
        for j in range(len(seq_list)):
            # If the sequence is the exact same, then we will not append it
            if seq_list[i] == seq_list[j]:
                pass
            else:
                # Compare the last 3 bases of one string to the first 3 bases of another string
                if seq_list[i][-3:] == seq_list[j][:3]:
                    # If they are the same, then append the ids to the pairs list as a list (i.e., nested list)
                    pairs.append([ids_list[i], ids_list[j]])

    # Create an output file with the pairs
    with open("grph_answer.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        for n in range(len(pairs)):
            file.write(" ".join(pairs[n]))
            file.write("\n")

overlap_graphs("rosalind_grph.txt")


