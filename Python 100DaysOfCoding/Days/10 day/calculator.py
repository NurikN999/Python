# from replit import clear
import art
print(art.logo)


#Calculator

def calculation(n1,operator,n2):
  if operator == '+':
    return n1 + n2
  elif operator == '-':
    return n1 - n2
  elif operator == '*':
    return n1 * n2
  elif operator == '/':
    return n1 / n2
  else:
    return "Error!"
def calculator():
  should_continue = True
  num1 = int(input("What's the first number?: "))
  print('+\n-\n*\n/')
  while should_continue:
    operator = input("What's operation yo want to do? ")
    num2 = int(input("What's the next number?: "))
    answer = calculation(num1, operator, num2)
    choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if choice == 'y':
      num1 = answer
    else:
      should_continue = False
      # clear()
      calculator()

calculator()