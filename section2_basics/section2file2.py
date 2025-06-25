def even(number):
    if number % 2==0:
        return True
    else:
        return False
    
print(even(75))
print(even(56))

def odd(number):
    return not even(number)
print(odd(75))

def checkevenlist(mylist):
    for _  in mylist:
        if _ % 2==0:
           return True
        else:
            pass
    return False
print(checkevenlist([1,3,5,7,9]))
print(checkevenlist([1,2,3,4,5]))

mylist=[("jose",12),("john",13),("joseph",14)]
def employeeoftheyear():
    workhour=0
    employeeoftheyear=""
    for name,workhours in mylist:
        if workhours>workhour:
            workhour=workhours
            employeeoftheyear=name
    return employeeoftheyear, workhour
result = employeeoftheyear()
print(result)

Stockprices=[("apple",200),("google",300),("microsoft",400)]
for item in Stockprices:
    print(item)

for stock,price in Stockprices:
    print(f"{stock} is at price of {price}")
    print(price)
    print(stock)

import random

mylist=["","O",""]
shuffled=random.shuffle(mylist)
print(mylist)
print(shuffled)#here we get None because shuffle() does not return anything, it just shuffles the list in place

def shuffle_list(mylist):
    random.shuffle(mylist)
    return mylist

shuffledlist=shuffle_list(mylist)
print(shuffledlist)

# args and kwargs

# ARGS
def myfunc(*args):
    print(sum(args) * 0.05)

myfunc(40,60)

def myfunc(**kwargs):
    if "fruit" in kwargs:
        print(f"my favourit fruit is {kwargs["fruit"]}")
    else:
        print("I do not have a favourite fruit")

myfunc(fruit="mango")

def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print(f"I would like {args[1]} {kwargs["fruit"]}")

myfunc(10,30,fruit="mango",vegetable="carrot",animal="dog")



               