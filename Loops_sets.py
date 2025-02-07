#LOOPS
x={"apple","banana", "cherry",True, 1, "ABC","Vedansh"}
for item in x:
    print(item)

# join sets
# 1) using union() method
# 2) using update() method

#union()
set1={"Vedansh", "Singh", "Akshay", 1}
set2={"Aarti", "Khanna", "Jack",2}

set3= set1.union(set2)
print(set3)

#update()
set1={"Vedansh", "Singh", "Akshay", 1}
set2={"Aarti", "Khanna", "Jack",2}

set1.update(set2)#this will add set2 items in set1
print(set1)

#Only DUPLICATES using intersection_update( ) function
set1={"Vedansh", "Aarti", "Akshay", 1}
set2={"Aarti", "Khanna", "Jack",1}

set1.intersection_update(set2)
print(set1)

#keep all but not duplicates
#using symmetric_difference_update() function

set1={"Apple", "Banana", "Cherry"}
set2={"Microsoft", "Google ","Apple","SHA1"}

set1.symmetric_difference_update(set2)# includes all set2 items and common items in set1
print(set2)



