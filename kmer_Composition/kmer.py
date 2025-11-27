import re
from itertools import product

def make_kmers_composition(dna_file):
    # Read-in the data file with the Sequence ID and DNA sequence
    dna = open(dna_file).read().replace('\n', '').split(">Rosalind_")

    dna = dna[1][4:]

    kmer_occurances = {}

    nucleotides = ["A", "C", "G", "T"]

    # Generate all possible kmers 
    kmers = [''.join(p) for p in product(nucleotides, repeat=4)]

    for kmer in kmers:
        kmer_occurances[kmer] = 0

    # Loop through all the kmers in the dna string
    for nt in range(len(dna) - 4 + 1):
        kmer = dna[nt:nt+4]

        if kmer in kmer_occurances.keys():
            kmer_occurances[kmer] += 1

    with open("kmer_answer.txt", "w") as f:
        for kmer in kmer_occurances.keys():
            f.write(str(kmer_occurances[kmer]) + " ")
    


make_kmers_composition("rosalind_kmer.txt")