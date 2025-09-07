
def findstrinDNA(fasta_file):
    data = open(fasta_file, "r").read().replace("\n", "").split(">Rosalind_")

    s = data[1]
    t = data[2]

    s = s[4:]
    t = t[4:]

    nos = 0
    num = ""

    for char in t:
        ##print(char)
        for n in range(len(s)):
            if s[n] == char and n > nos:
                nos = n
                char += char
                num += str(n+1) + " "

    with open("sseq_answer.txt", 'w') as file:
        file.write(num)
    

findstrinDNA("rosalind_sseq.txt")

