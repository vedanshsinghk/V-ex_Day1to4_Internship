#
myset={"apple","banana", "cherry"}
print(myset)

#type
print(type(myset))

#duplicates not allowed
# Banana and banana are two different keywords
#because of the case sensitveness
set1={"apple","Banana","cherrry","Banana"}
print(set1)

#get length
print("The length of set 'myset' is: ",len(myset))
print("The length of set 'set1' is:  ",len(set1))

#Data Types
set2={"ABC", "Vedansh", 1,2,3, True}
print(set2)

#add items
set2={"ABC", "Vedansh", 1,2,3, True}
set2.add("orange")
print(set2)

#add items using update() function
set2={"ABC", "Vedansh", 1,2,3, True}
set3= {"Pineapple", "Jamun","Berry"}
set2.update(set3)#items in set2 will be updated and set3 items will be added
print("The latest set2 is:", set2)

#remove items
set2={"ABC", "Vedansh", 1,2,3, True}
set2.remove("Vedansh")
print("Set2 after removal is: ",set2)

#remove random item using pop() function
set2={"ABC", "Vedansh", 1,2,3, True}
x=set2.pop()
print("Random item is:",x)
print( "And now set is: ",set2)

#clear set()
x={"apple","banana", "cherry",True, 1, "ABC","Vedansh"}
x.clear()
print(x)

#del set using "del" keyword
x={"apple","banana", "cherry",True, 1, "ABC","Vedansh"}
del x

