import math

def partialPerm (file):
    # Read in file ad get n and k
    data = open(file).read().split(" ")

    # n is the first number and k is the second number
    n = int(data[0])
    k = int(data[1])

    # Create an output file with the pairs
    with open("pper_answer.txt", 'w') as file:
        # The formula for partial factorial is n!/(n-k)!
        file.write(str(int((math.factorial(n)/math.factorial(n-k)) % 1000000)))

partialPerm("rosalind_pper.txt")




