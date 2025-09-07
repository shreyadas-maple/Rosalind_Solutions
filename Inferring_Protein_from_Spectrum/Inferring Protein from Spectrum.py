# import the string module to check if a string is a letter
import string

def monoisotopicMassTable(table_file):
    # Read in the Monoisotopic Mass Table from a txt file
    table = open(table_file).read().replace('\n', ' ').split(" ")

    # Grab all the uppercase letter in string data type
    letters = string.ascii_uppercase

    # Initialize an empty dictionary
    mass_table = {}

    # Populate the mass_table dictionary to have the mass as the key and the amino acid as the value
    for i in range(len(table) - 1):
        # Check if the current item in the table list is a letter
        if table[i] in letters:
            # If it is a letter, then get the mass which is the number after the letter
            # Because the mass is a string we have to cast it as a float and then round to 2 decimal places
            mass = round((float(table[i + 1])), 2)

            # Populate the dictionary with the "mass" : "amino acid"
            mass_table[mass] = table[i]
    
    # Return the mass_table dictionary to the function call
    return mass_table

# Create a function to infer the protein string
def inferProtein(file):
    # Get the protein string masses from the file
    data = open(file).read().replace('\n', ' ').split(" ")

    # Remove the last item in data, because it is a " ", which will not be recognized as number
    data = data[:-1]

    # Get the mass_table using the function call to the text file
    mass_table = monoisotopicMassTable("Monoisotopic Mass Table.txt")

    # Intialize an empty string to save the protein string
    protein_str = ""

    # Loop through the data provided to find the differences between the protein strings
    for j in range(len(data) - 1):
        # Cast the next number number and current number as float and then round the difference 
        # to 2 decimal places
        diff = round((float(data[j + 1]) - float(data[j])), 2)

        # Get the amino acid from the mass_table dictionary using the diff as the key value
        amino_Acid = mass_table[diff]

        # Add the amino acid letter to the protein string
        protein_str += amino_Acid

    # Create an output file
    with open("spec_ans.txt", 'w') as file:
        # Write the protein in the file
        file.write(protein_str)

inferProtein("rosalind_spec.txt")