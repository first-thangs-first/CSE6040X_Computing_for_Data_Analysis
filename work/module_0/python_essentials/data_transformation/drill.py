names = ["Peter", "Lois", "Meg", "Chris", "Stewie", "Brian"]
ages = [41, 40, 16, 17, 1, 18]
"""
Assume that the ages in ages correpond to the names in names by index. Write a Python module which:

Assigns to the variable family a list of tuples in which the first element of each tuple is a name and the second element is the associated age.
Assigns to the variable name2age a dictionary mapping names to ages.
Assigns to the variable sorted_family the elements of family sorted by age.
Assigns to the variable adults the members of family with an age of 18 or greater.
"""

family = [(names[index], ages[index]) for index in range(len(names))]
name2age = {names[index]: ages[index] for index in range(len(names))}
sorted_family = sorted(family, key=lambda member: member[1])
adults = [member for member in family if member[1] >= 18]