def countSubsets(file):
    # Read in n from the input file
    n = open(file).read()

    # The total number of subsets of {1, 2, ..., n} is 2**n
    # We have to do mod 1,000,000 from instructions of the problem
    num_subsets = (2 ** int(n)) % 1000000

    # Create an output file
    with open("sset_answer.txt", 'w') as file:
        file.write(str(num_subsets))

countSubsets("rosalind_sset.txt")