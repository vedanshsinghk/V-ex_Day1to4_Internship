thislist = ["apple", "banana", "cherry","Grapes", "Pineapple"] 
thislist[1:3] = ["watermelon"]  

#index 1 is included and 3 index not as per slicing rule
#so index 1 and index 2 are sliced
#in return we get watermelon instead of (banana and cherry)
print(thislist) 

