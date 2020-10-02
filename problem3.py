"""
Problem 3:
input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

number = int(input("Enter a number that is smaller than 10: "))
y = 0
print("the sum of the series is", end = " ")

for i in range(1, number+1):
    y = y+1
    z = str(y)
    print(z, end= "")

