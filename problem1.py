"""
Problem1:
inputs:
int number

outputs:


example:
enter a number:4
****
****
****
****
"""


x = int(input("Enter a number: "))
y = ("*")

for i in range(x):
    print(y*x)