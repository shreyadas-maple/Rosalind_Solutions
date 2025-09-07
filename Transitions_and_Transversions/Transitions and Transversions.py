def hamming_dist(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    num_diff = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            num_diff += 1
        else:
            num_diff += 0

    return num_diff


def trans(fasta_file):
    data = open(fasta_file, "r").read().replace("\n", "").split(">Rosalind_")

    str1 = data[1][4:]
    str2 = data[2][4:]

    dist = hamming_dist(str1, str2)

    transit = 0

    for (char, txt) in zip(str1, str2):
        if (char == "A" and txt == "G") or (char == "G" and txt == "A") or (char == "C" and txt == "T") or (char == "T" and txt == "C"):
            transit += 1

    transverse = dist - transit

    with open("tran_answer.txt", 'w') as file:
        file.write(str(transit/transverse))

trans("rosalind_tran.txt")