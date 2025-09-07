def comTree(file):

    # Get the data from the file
    data = open(file).read().replace("\n", " ").split(" ")

    # Initialize the variable n to store the number of nodes
    n = 0

    # Remove the last item in data because it is a blank " "
    # This will give us errors down the line
    data.pop(len(data) - 1)

    # Initialize list with the node connections
    node_connections = []

    # Populate the n and node_connections variables
    for i in range(0, len(data)):
        if i == 0:
            # The first number in data is n
            n = int(data[0])
        else:
            # The other numbers are the node connections
            node_connections.append(int(data[i]))
    
    # The number of connections is the number of nodes / 2
    num_connections = int(len(node_connections) / 2)

    # the total minimum number of connections in a tree is n - 1
    num_min_connections = n - 1

    # Create an output file
    with open("tree_ans.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(num_min_connections - num_connections))

comTree("rosalind_tree.txt")
