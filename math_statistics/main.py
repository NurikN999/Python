import math
from scipy.stats import binom
import matplotlib.pyplot as plt


def color_bar(n , condition_type):
    number = int(condition_type[-1])
    colors = []
    if "<=" in condition_type:
        for i in range(n + 1):
            if i <= number: colors.append("#FF0000")
            else: colors.append("#0000FF")

    if ">=" in condition_type:
        for i in range(n + 1):
            if i >= number: colors.append("#FF0000")
            else: colors.append("#0000FF")

    if ">" in condition_type:
        for i in range(n + 1):
            if i > number: colors.append("#FF0000")
            else: colors.append("#0000FF")

    if "<" in condition_type:
        for i in range(n + 1):
            if i < number: colors.append("#FF0000")
            else: colors.append("#0000FF")

    return colors

dist = []
n = int(input("Enter n: "))
p = float(input("Enter p: "))
condition = input("Do you have any condition? Type 'yes' or 'no': ").lower()
if condition == 'yes':
    condition_type = input("Enter condition to x: ")
condition_type = "x<=0"

# defining the list of x values
x = list(range(n + 1))


def binomial_distribution(x, n, p):
    return (math.factorial(n) / (math.factorial(x) * math.factorial(n - x))) * (math.pow(p,x) * math.pow(1 - p, n - x))
# defining the E(expected value), V, q, Variance
E = n * p
q = 1 - p
V = E * q
variance = math.pow(V, 0.5)
# list all probability
for i in x:
    dist.append(binomial_distribution(i,n,p))
print("x\tp(x)")
for i in range(n + 1):
    print(str(x[i]) + "\t" + str(dist[i]))
print()
print(f"E: {E} \nV: {V} + \nQ: {variance}")
plt.bar(x, dist , color = color_bar(n, condition_type))
plt.show()