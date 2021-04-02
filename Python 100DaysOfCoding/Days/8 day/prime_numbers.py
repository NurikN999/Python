
def prime_number_check(number):
	divider = 2
	is_not_prime = False
	while(divider <= number / 2):
		if number % divider == 0:
			is_not_prime = True
			break
		divider += 1
	if not is_not_prime:
		print(f"{number} is a prime number")
	else:
		print(f"{number} is not a prime number")

number = int(input("Enter a number: "))
prime_number_check(number)