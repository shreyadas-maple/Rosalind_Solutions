from urllib.request import urlopen
def getfasta(uniprot_id):
    url = "http://www.uniprot.org/uniprot/" + uniprot_id[:6] +".fasta"
    page = urlopen(url).read().decode('utf-8').split("\n")
    fasta = page[1:]
    fasta_seq = "".join(fasta)
    loc = []
    prot_seq = []

    for i in range(len(fasta_seq) - 4):
        if fasta_seq[i] == "N" and fasta_seq[i+1] != "P" and (fasta_seq[i + 2] == "S" or fasta_seq[i+2] == "T") and fasta_seq[i+3] != "P":
            loc.append(i+1)
            prot_seq.append(fasta_seq[i:i+4])
    return loc

def domain(FASTA_file):
    file = open(FASTA_file).read().split("\n")
    ids = []

    for line in file:
        ids.append(line)

    # Create an output file with the pairs
    with open("mprt_answer.txt", 'w') as file:
        for id in ids:
            prot_loc = getfasta(id)
            if prot_loc != []:
                file.write(id)
                file.write("\n")
                string = ""
                for loc in prot_loc:
                    string += str(loc) + " "
                file.write(string)
                file.write("\n")

domain("rosalind_mprt.txt")

