from itertools import product

def make_kmers_composition(dna_file):
    # Read-in the data file with the Sequence ID and DNA sequence
    dna = open(dna_file).read().replace('\n', '').split(">Rosalind_")

    # Get only the dna sequence from the file that is read-in
    dna = dna[1][4:]

    # Initialize an empty dictionary to hold all the occurances of each kmer
    kmer_occurances = {}

    # Create a list of all the nucleotides in lexicographical order
    nucleotides = ["A", "C", "G", "T"]

    # Generate all possible kmers using product
    kmers = [''.join(p) for p in product(nucleotides, repeat=4)]

    # Initialize all the possible kmers in the empty dictionary with a value of 0
    for kmer in kmers:
        kmer_occurances[kmer] = 0

    # Loop through all the kmers in the dna string
    for nt in range(len(dna) - 4 + 1):
        # The kmer in the dna string is obtained using string slicing
        kmer = dna[nt:nt+4]

        # If the kmer that is made from the dna string is in the kmer_occurances dictionary
        if kmer in kmer_occurances.keys():
            # Add one to its value
            kmer_occurances[kmer] += 1

    # Create a file with the kmer occurances 
    with open("kmer_answer.txt", "w") as f:
        # By looping through all the kmers in the kmer_occurances dictionary
        for kmer in kmer_occurances.keys():
            # And writing its occurances in the file
            f.write(str(kmer_occurances[kmer]) + " ")

# Function call to the input text file
make_kmers_composition("rosalind_kmer.txt")