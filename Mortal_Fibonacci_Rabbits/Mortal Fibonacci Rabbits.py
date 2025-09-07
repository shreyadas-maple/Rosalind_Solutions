# We are going to solve this problem using dynamic programming

def numberRabbits (n, m):
    # We create a list to store the number of rabbits in each stage of life
    # [0] -> newborns; [1] -> rabbits that are 1-month old; [m-1] -> rabbits that are m-1 months old
    rabbits = [0] * m

    # In the first month, there is 1 rabbit
    rabbits[0] = 1

    # We are going to iterate through the months 
    for i in range(1, n):
        # Save the number of new_borns each month
        new_borns = 0
        # Iterate through each life stage, to calculate the number of new_borns
        for j in range (1, m):
            # If there are rabbits that are able to reproduce, then add the new borns
            if rabbits[j] > 0:

                new_borns += rabbits[j]
        
        # We insert new_borns as the first index of the list
        rabbits.insert(0, new_borns)
        # We remove the last index of the last, because in the previous month
        # these are the rabbits that have reached the last month of their life
        rabbits.pop()

    # Create an output file
    with open("fibd_ans.txt", 'w') as file:
        file.write(str(sum(rabbits)))

num = list(open("rosalind_fibd.txt").read().replace('\n', ' ').split(" "))

n = int(num[0])
m = int(num[1])

numberRabbits(n, m)