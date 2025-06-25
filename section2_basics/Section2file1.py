# COMPARISIONS OPERATORS
print(6==7)#false
print(6==6)#true
# here == is  used to prouf equality btw 2  variable or numbers
print("BYE==BYe")#false because of case sensitivity
print("BYE"=="BYE")#true    
# != is not equal to 
print(53!=53)#false because both are equal
print(53!=54)#true because both are not equal
# > is greater than and < is less than
print(73>29)#true because 73 is greater than 29
print(73<29)#false because 73 is not less than 29
# >= is greater than or equal to and <= is less than or equal to
print(99>=74)#true because 99 is greater than 74
print(99>=99)#true because 99 is equal to 99

# <= is less than or equal to
print(99<=74)#false because 99 is not less than 74
print(99<=99)#true because 99 is equal to 99

# logical operators
# AND operator
print(99==99 and 5>2)#true because both conditions are true
print(99==99 and 5<2)#false because second condition is false
# OR operator
print(99==99 or 84>100)#true because first condition is true
print(99==999 or 84>100)#false because none of the statements is true
# NOT operator
print(not(99==99))#false because 99 is equal to 99
# basically it returns the opposite boolean


# STATEMENTS 
if  99==99:
    print("its equal to 99")
else:
    print("its not equal to 99")

if  98==99:
    print("its equal to 99")
else:
    print("its not equal to 99")

name="john"
if name=="frankie":
    print("hello frankie")
elif name=="joseph":
    print("hello joseph")
else:
    print("what is your name")
    name="frankie"
if name=="frankie":
    print("hello frankie")
elif name=="joseph":
    print("hello joseph")
else:
    print("what is your name")

# LOOPS
# for loop
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for num in numbers:
    if num%2==0:
        print(num)

mystring="hello world"
for _ in mystring:
    print(_)

mytup=(1,2,3,4,4,5,6,7,8,9,10)
for item in mytup:
    print(item)

mylist=[(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mylist:
     print(f"{a}\n{b}\n{c}")    
    #  this is tuple unpacking

# while loop
while True:#true can be any statement that is true
    print("hello world")
    break  # this will break the loop after one iteration, otherwise it will run infinitely

a=0
while not a<10:
    print(a)
    a+=1  # this will increment the value of a by 1 after each iteration
    

    # IMPORTANT FUNCTIONS
a=list(range(1,11))
print(a)
# this will create a list of numbers from 1 to 10   

    # enumerate function
mylists=["a","b","c","d","e"]
for x,y in enumerate(mylists):
     print(x,y)
       

# zip function
mylist1=[1,2,3,4,5]
mylist2=["a","b","c","d","e"]
for x,y in zip(mylist1,mylist2):
    print(x,y)

# in operator
mylist=[1,2,3,4,5]
if 92 in mylist:
    print("92 is in the list")
else:
    print("92 is not in the list")

# min and max functions
mylist=[1,2,3,4,5]
print(min(mylist))  # this will print the minimum value in the list
print(max(mylist))  # this will print the maximum value in the list

# random module
import random   
print(random.randint(1,100))  # this will print a random number between 1 and 100

mylist=[]
mystring="hello world"
for _ in mystring:
    mylist.append(_)
print(mylist)  # this will print the list with the string "hello world" repeated for each element in mylist

def sayhello(name="John"):
    print(f"hello {name}")
sayhello()  # this will print "hello John" because the default value of name is "John"
sayhello("mike")    # this will print "hello mike" because we passed the value "mike" to the function

def add(a,b):
    print(a+b)
add(10,20)

def returnadd(a,b):
    return a+b
print(returnadd(40,60))  # this will print the result of the addition of 40 and 60, which is 100
result=returnadd(20,20)
print(result)  # this will print the result of the addition of 20 and 20, which is 40





