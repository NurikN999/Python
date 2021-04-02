import art
print(art.logo)
print("Welocme to the secret auction program.")



def add_person(name, bid):
	new_person = {}
	new_person[name] = bid
	list_of_people.append(new_person)


list_of_people = []
name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
add_person(name,bid)

other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
while other_bidders == 'yes':
	name = input("What is your name?: ")
	bid = int(input("What's your bid?: $"))
	add_person(name,bid)
	other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
	if other_bidders == 'no':
		break

list_of_cash = []
for i in range(len(list_of_people)):
	for key in list_of_people[i]:
		list_of_cash.append(list_of_people[i][key])

max_cash = list_of_cash[0]
for i in range(len(list_of_cash)):
	if list_of_cash[i] > max_cash:
		max_cash = list_of_cash[i]

for i in range(len(list_of_people)):
	for key in list_of_people[i]:
		if list_of_people[i][key] == max_cash:
			print(f"The winner is {key} with a bid of ${list_of_people[i][key]}")