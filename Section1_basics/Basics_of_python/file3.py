# DICTIONARIES
mydict={'f1':'apple', 'f2':'banana', 'f3':'cherry', 'f4':'date', 'f5':'elderberry'}
print(mydict)
print(mydict["f1"])
# dictionaries can hold list constants strings and other dictionaries
mydict2={'k1':'hiddenkey',"k2":[4,3,5,6,13,7],"k3":{"ikey":"hello world1", "ik2":"hello world2"}}
print(mydict2)
print(mydict2["k2"][3])
print(mydict2["k3"]["ikey"])

d1={"k1":200,"k2":300}
print(d1)

d1["k3"]=400
print(d1)
# here we addwd a new key and value to the dictionary
d1["k1"]=100
print(d1)
# here we changed the key and the value
 
print(d1.keys())
print(d1.values())
print(d1.items())

# TUPLES
t1=(1,2,3,4,5,6,7,8,9,10)

print(t1.count(6))
print(t1.index(3))

# SETS
set1= set()
print(set1)
set1.add(1)
print(set1)

# BOOLEANS
print(18>9)
print(type(set1))