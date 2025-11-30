# Import factorial function
from math import factorial

def num_combos (a, b):
    # This function calculates the number of combinations for a and b. 
    # Input: int a total number of items and b number of items to choose
    # Output: int of the number of combinations

    # Formula to calculate the number of combination using the Combination statistic
    num = factorial(a) // (factorial(b)*(factorial(a-b)))

    # Return the total number of combinations
    return num


def find_combos_isoforms(file):
    # This function returns the sum of the total number of combinations from a m to n
    # Input: file containing m and n
    # Output: file containing total number of combinations from m to n

    # Get the data from the file that is given
    data = open(file, 'r').read().strip().split(' ')

    # In the file the first number is and second number is m
    n = int(data[0])
    m = int(data[1])

    # Initialize a variable to hold the sum of the combinations
    tot_com = 0

    # Loop through the fixed number items to choose from n
    for k in range(m, n + 1):
        # Add the calculated number of combinations for a fixed k 
        tot_com += num_combos(n, k)
    # The final number has to be mod 1000000
    mod_sum = int((tot_com) % 1000000)

    # Write the final number to a output file
    with open("aspc_answer.txt", "w") as f:
        f.write(str(mod_sum))

# Function call 
find_combos_isoforms("rosalind_aspc.txt")