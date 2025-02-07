#keys
car = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = car.keys() 
print("Before change: ", x) #before  change 
car["color"] = "white" # this will add ine more entity
print("After change: ",x) # after change

# values
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = thisdict.values() 
print(x) 

#items (means collection of keys:values)
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = thisdict.items() 
print(x)

#using if statement:
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
if "color" in thisdict: 
    print("Yes, 'model' is one of the keys in the thisdict dictionary") 
else:
    print("No such item present in Dictionary")

#change dictionary items
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
thisdict["year"] = 2018 
print(thisdict)

#add dictionary items
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
thisdict["color"] = "red" 
print(thisdict) 

#Remove dictionary Items using pop() functin
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
thisdict.pop("model") 
print(thisdict)

#Remove Dictionary items using pop.tem() function
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
thisdict.popitem() 
print(thisdict)

#delete dictionary using del keyword
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
del thisdict["model"] 
print(thisdict)

#clear dictionary
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
thisdict.clear() 
print(thisdict)