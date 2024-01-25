"""
Given a list of names, create a dictionary where the keys are names and the values are the lengths of the 
corresponding names.
"""
# List of names
names = ["Surajan", "Milan", "Avay", "Sid", "Shishir"]

# Create an empty dictionary
name_lengths = {}

# Populate the dictionary with names and their lengths
for name in names:
    name_lengths[name] = len(name)

# Display the resulting dictionary
print(name_lengths)
