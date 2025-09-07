
from difflib import SequenceMatcher

def parseFASTA(fastaFile):
    ## We will save all the ids in one array
    id_list = []

    ## Save all the sequences in a separate array
    seq_list = []

    ## Open the file and replacing all the newlines and split the data where a new sequence starts
    data = open(fastaFile).read().replace('\n', '').split(">")
    newdata = data[1:]

    ## Based on when Rosalind appears in the array of data, we sort into ids or sequences
    for i in range(0, len(newdata)):
        if newdata[i].startswith("Rosalind"):
            id_list.append(newdata[i][0:13])
            seq_list.append(newdata[i][13:])

    ## Since we are only going to use the sequence array, return the sequence array only
    return seq_list

def findSharedMotif(list_seq):
    ## We need to find the length of the array of sequences or how many sequences do we need to look through
    arr_n = len(list_seq)

    ## Use the first sequence to check through all the other seqeunces
    first = list_seq[0]

    ## Length of the first sequence in the array of sequences
    first_n = len(first)

    ## This is where we will store the common string, once it is found; we will return this at the end
    common_str = ""

    ## We are going to iterate through the first sequence in the array
    for i in range(first_n):
        for j in range(i + 1, first_n + 1):
            ## generating all substrings of the first sequence
            word = first[i:j]
            k = first_n
            for k in range(1, arr_n):
                ## Using not in, we are checking if the generated substring is not in all of the
                ## sequences of the array
                if word not in list_seq[k]:
                    ## If it is not common in all sequences, then it will exit the for loop
                    ## and move on to generating the next substrings
                    break
            ## If it reaches here, then the current stem is common to all sequences, we need to check
            ## if it is longer than the current common string
            if (k + 1 == arr_n and len(common_str) < len(word)):
                common_str = word
    ## return the longest common string of the array
    # Create an output file with the pairs
    with open("lcsm_answer.txt", 'w') as file:
        file.write(common_str)

findSharedMotif(parseFASTA("rosalind_lcsm.txt"))