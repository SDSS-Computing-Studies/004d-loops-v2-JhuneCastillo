x = input("Enter a username: ")

nameList = ("Lebron","Kobe","Michael","Shaq","Dennis")

for i in nameList:
    if i == x:
        print("That name is in the list")
        
if x not in nameList:
        print("That name is not in the list")
       


