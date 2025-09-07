def findSubPerm (file):
    data = open(file).read().replace('\n', ' ').split(" ")

    print(data)

    n = data[0]
    pi = data[1:]

    # Find the increasing subsequence
    increase = []


findSubPerm("rosalind_lgis.txt")