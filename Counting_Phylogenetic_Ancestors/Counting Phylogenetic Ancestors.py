def num_ancestors(file):
    # Get the number of leaves from reading in the file
    num_leaves = int(open(file).read())

    # Calculate the number of internal nodes for an unrooted binary tree
    # which is n - 2, where n is the number of leaves
    num_internal = num_leaves - 2

    # Make a file with the number of internal nodes
    with open("inod_ans.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(num_internal))

num_ancestors("rosalind_inod.txt")