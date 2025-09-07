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

# Function to calculate the Hamming distance between 2 sequences
def hamming_dist(str1, str2):
    # Convert both DNA sequences to upper
    str1 = str1.upper()
    str2 = str2.upper()

    # Initialize a variable to save the number of differences
    num_diff = 0

    # Loop through each string and compare both strings to 
    # count the number of differences
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            num_diff += 1
        else:
            num_diff += 0
    # Return the number of differences
    return num_diff

# Function to create the distance matrix
def distMatrix(file):

    # Parse the file to get a list of DNA sequences
    sequences = parseFASTA(file)

    # Get the number of sequences to help with looping through rows and cols
    num_seq = len(sequences)

    # Get the length of the first sequence to calculate the p-distance
    seq_len = len(sequences[0])

    # Write the file formatted in a matrix way
    with open("pdst_ans.txt", 'w') as file:
        # Loop through the rows
        for rows in range(num_seq):
            # row is the row in the matrix of the output file
            row = ""
            # Loop through the cols of the matrix
            for cols in range(num_seq):
                # Calculate pdist by calculating Hamming distance and then divide by the sequence length
                pdist = hamming_dist(sequences[rows], sequences[cols]) / seq_len
                # Format the pdist to have at max 5 decimal places
                pdist = f"{pdist:0.5f}"

                # If it is the last col of the matrix, don't add a space at the end of the row
                if cols == num_seq - 1:
                    row += str(pdist)
                # Else it is not the last col of the matrix, then add a space
                else:
                    row += str(pdist) + " "
            # At the end of the row we need to move to the next line
            row += "\n"
            # Write the row in the file
            file.write(row)
            
distMatrix("rosalind_pdst.txt")