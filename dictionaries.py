
#DICTIONARIES
mydict={
    "brand": "ford",
    "Model": "Mustang",
    "Year": 1964
}
print(mydict)

#length
mydict={
    "brand": "ford",
    "Model": "Mustang",
    "Year": 1964
}
print(len(mydict))

#
thisdict = { 
"brand": "Ford", 
"electric": False, 
"year": 1964, 
"colors": ["red", "white", "blue"] 
} 
print(thisdict)

#type
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
print(type(thisdict))

#
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = thisdict["model"] 
print(x)
#using get() method
y = thisdict.get("model") 
print(y)

#get keys using .keys() function
thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
}
x= thisdict.keys()
print(x)

