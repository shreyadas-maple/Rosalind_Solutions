
def numberRabbits (n, k):

    if n == 1 or n == 2:
        return 1
    else:
        twoGen = numberRabbits(n - 2, k)
        oneGen = numberRabbits(n - 1, k)

        return twoGen * k + oneGen
    

n, k = open("rosalind_fib.txt").read().split(" ")

n, k = int(n), int(k)

# Create an output file with counts
with open("fib_ans.txt", 'w') as file:
    # Format the print of the pairs according to instructions
    file.write(str(numberRabbits(n, k)))