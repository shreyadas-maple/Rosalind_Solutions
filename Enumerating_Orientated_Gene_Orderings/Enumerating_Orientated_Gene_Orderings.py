from itertools import permutations, product, combinations

def orientatedGenePerms(file):
    # Get the n value from the file
    n = int(open(file).read())

    # This is the final list with all the permutations
    num_list = []

    # Contains the list of unsigned number to then have signs put on them
    unsigned_nums = []

    # We will loop through the range of 1 to n+1
    for i in range(1, n + 1):
        # Then append each number to the unsigned_nums listß
        unsigned_nums.append(i)

    # Create a base list of number with all the permutations of the unsigned numbers
    # This will create a list of tuples
    base_list = list(permutations(unsigned_nums, n))

    # Make a list of tuples with combinations of -1 and 1
    signs = list(product([-1, 1], repeat =n))

    # Loop through the the base list with the permutations
    for perm in base_list:

        # Loop through the list with the sign permutations
        for sign in signs:

            # Multiply the list from the base list and the sign together
            result_tuple_comp = list(a * b for a, b in zip(perm, sign))
            
            # Append the result tuple to the final list
            num_list.append(result_tuple_comp)

    # Get the total number of permutations
    total = len(num_list)

    # Create an output file
    with open("sign_ans.txt", 'w') as file:
        # Write the lines in the text file
        total_line = str(total) + "\n"

        # Write the total of the premutations in the file
        file.write(total_line)

        # Loop through the list of permutations
        for i in num_list:
            # Start with a blank string
            line = ""
            # Loop through each list element
            for j in i:
                # Add the string of the integer in the number list with a space after
                line += str(j) + " "
            # Enter a new line at the end of the permutation
            line += "\n"
            # Write the line in the file
            file.write(line)

orientatedGenePerms("rosalind_sign.txt")


