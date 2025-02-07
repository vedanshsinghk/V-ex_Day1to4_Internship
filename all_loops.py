#SHORT HAND IF :

a=10 
b=5
if a>b: print("A is greater than B")

#SHORT HAND IF ELSE
a= int(input("Enter your number A= "))
b= int(input("Enter your number B= "))
print(a) if a>b else print(b)

# Ternary opertors or COnditional 
a = 330 
b = 330
print("A") if a > b else print("=") if a == b else print("B") 

# and
a= int(input("Enter your number A= "))
b= int(input("Enter your number B= "))
c= int(input("Enter your number C= "))
if a>b and c>a:
    print("Both conditions are true")

# Or
a= int(input("Enter your number A= "))
b= int(input("Enter your number B= "))
c= int(input("Enter your number C= "))
if a>b or a>c:
    print("atleast one condition is satisfied")
else:
    print("Your entered Choice is wrong")

# NOT
a= int(input("Enter your number A= "))
b= int(input("Enter your number B= "))

if not a > b: 
    print("a is NOT greater than b")
else:
    print("A is greater than B")

# Nested if:
x=int(input(" Enter you number X= "))
if x > 10: 
    print("Above ten,") 
    if x > 20: 
        print("and also above 20!")     
else: 
    print("but not above 20.")

#For Loops
fruits = ["apple", "banana", "cherry"] 
for x in fruits: 
    print(x)

for x in "banana": 
    print(x)

#break statement
fruits = ["apple", "banana", "cherry"] 
for x in fruits: 
    print(x)
    if x == "banana": 
        break
# continue statement
fruits = ["apple", "banana", "cherry"] 
for x in fruits: 
    if x == "banana": 
        continue 
    print(x) 

