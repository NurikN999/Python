#So, there is "TypeError", when we try to input into "len()" function an integer
len(123456)

# #Also, we will have error if will try to concatenate String with Integer, like in example below:
name = input("What is your name?: ")
print("Your name length is " + len(name))

#We can check "type" of our variable by putting variable into type() function
num = 89
print(type(num))