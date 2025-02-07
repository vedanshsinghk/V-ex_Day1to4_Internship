thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
for x in thisdict:
    print(thisdict[x])

# for values 
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
for x in thisdict.values(): 
    print(x) 

#for keys
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
for x in thisdict.keys(): 
    print(x)

#for items
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
for x, y in thisdict.items(): 
    print(x,y)

#copydictionaries

thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
mydict = thisdict.copy() 
print(mydict)

