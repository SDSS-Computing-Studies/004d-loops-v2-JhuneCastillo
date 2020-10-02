"""
Problem 2:
inputs:
int number

outputs:
"xx! is yy" where xx is the integer entered and yy is the calculated answer

example:
Enter a number: 4
4! is 24
"""

number = int(input("Enter a number: "))
x = str(number)
y = 1 

for i in range(1, number+1):
    y = y*i
    
y = str(y)
print(x + "! is " + y)