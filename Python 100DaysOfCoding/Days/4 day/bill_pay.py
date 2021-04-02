import random as r
name_string = input("Give me eerybody's names, separated by a comma. ")
names = name_string.split(", ")

print(r.choice(names) + " will pay today!")