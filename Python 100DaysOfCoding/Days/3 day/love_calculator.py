name1 = input("What is your name?: ")
name2 = input("What is their name?: ")

counter_true = 0
counter_love = 0

name1 = name1.lower()
name2 = name2.lower()

counter_true += name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name2.count("t")+ name2.count("r")+ name2.count("u")+ name2.count("e")
counter_love += name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") + name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

percentage = str(counter_true) + str(counter_love)
print(f"Your score is {percentage}")