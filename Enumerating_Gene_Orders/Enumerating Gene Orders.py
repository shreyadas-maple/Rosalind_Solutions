from itertools import permutations

def permut(num):

    perm = permutations(range(1, num + 1))
    count = 0

    empty = []

    for i in list(perm):
        count += 1
        empty.append(i)

    # Create an output file with the pairs
    with open("perm_answer.txt", 'w') as file:
        file.write(str(count))
        file.write("\n")
        for tup in empty:
            line = ""
            for i in list(tup):
                line += str(i) + " "
            file.write(line)
            file.write("\n")

num = open("rosalind_perm.txt").read()

permut(int(num))


