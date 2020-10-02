x = input("Enter a name: ")

nameList = ("Lebron","Kobe","Michale","Shaq","Dennis")

for i in nameList:
    if i == x:
        print("That name is on the list")
        
if x not in nameList:
        print("That name is not on the list")
       


