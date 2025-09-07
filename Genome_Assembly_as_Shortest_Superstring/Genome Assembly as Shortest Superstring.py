
def parseFASTA(fastaFile):
    # Save all the sequences in a separate list
    seq_list = []

    # Open the file and replacing all the newlines and split the data where a new sequence starts
    data = open(fastaFile).read().replace('\n', '').split(">")
    newdata = data[1:]

    # Based on when Rosalind appears in the array of data, we append the sequences and IDs to the
    # respective lists
    for i in range(0, len(newdata)):
        seq_list.append(newdata[i][13:])

    # Return the sequence and IDs list
    return seq_list

def findOverlap (s1, s2, min_overlap):
    # We are checking if the suffix of s1 is the prefix of s2

    # The max overlap is the minimum of the 2 sequences
    max_overlap = min(len(s1), len(s2))


    for i in range(max_overlap, min_overlap - 1, -1):
        # Check if the suffix of s1 is equal to the preffix of s2
        # if so return the index of the start of the overlap 
        if s1[-i:] == s2[:i]:
            return i
    return 0

# This function adds the sequences up
def addSeq(edge_weights, connections, sequences):

    # We will save the connections in order ex. [31, 32] [32, 0]
    # This is in order because 31 -> 32 which 32 -> 0
    in_order = []

    # This is for the last sequence, since it has no suffix
    j = "-"

    # Loop through the connections to find the key (string with suffix)
    # associated with the value (string with preffix)
    for i in range(len(connections)):
        # We use a function to find the key
        r = findKey(connections, j)
        # Insert it as the first element in the list of ordered connections
        in_order.insert(0, [r, j])
        # the next connection to look for is the key for this iteration of the loop
        j = r
    
    # The first sequence to be added to the final sequence is the first sequence in
    # the in_order list 
    final_Seq = str(sequences[in_order[0][0]])

    # Loop through the the in_order list
    for i in range(0, len(in_order) - 1):
        # Get the next sequence in order
        s1 = sequences[in_order[i + 1][0]]
        
        # Get the weight for the next sequence
        weight = edge_weights[in_order[i][0]]

        # Add the preffix of the next sequence in order
        final_Seq += s1[weight:]

    # Return the final sequence
    return final_Seq

# This is the function to find the key for a value in a dictionary
def findKey (dictionary, target):

    for key, item in dictionary.items():
        if item == target:
            return key
            
    return -1
    

def assemblySuperstring (file):
    # Get the data from the file
    data = parseFASTA(file)

    # Make nodes for all the sequence numbers
    nodes_index = list(range(0, len(data)))

    # Make a graph for the weights in the connections
    edge_weights = {}

    # Make a graph with the connections of the nodes
    connections = {}

    # Loop through the nodes
    for i in nodes_index:
        weights = -1
        # Loop through the nodex to find the sequences that overlap
        for j in nodes_index:
            # If there are the same exact sequences then ignore
            if data[i] == data[j]:
                pass
            else:
                # m is the minimum overlap required
                m = int(min(len(data[i]), len(data[j])) / 2)
                # w is the weight calculated by the function findOverlap
                w = (findOverlap(data[i], data[j], m))

                # If the overlap is not 0 then add it to edge_weights
                if w != 0:
                    weights = w
                    # That node's connection is the sequence that has overlap
                    connections[i] = j
        edge_weights[i] = weights

    # Loop through the edge weights to find the sequence with no overlap, with 
    # any other sequence and add a "-"
    for i in range(0, len(edge_weights)):
        if edge_weights[i] == -1:
            connections[i] = "-"
    
    # Call the addSeq function to add the sequences according to the edge_weights,
    # connections, and data
    final_seq = addSeq(edge_weights, connections, data)

    # Write an output file with the final_seq
    with open("long_answer.txt", 'w') as file:
        file.write(final_seq)

assemblySuperstring("rosalind_long.txt")




