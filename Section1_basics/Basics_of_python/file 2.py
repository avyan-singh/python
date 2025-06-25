x="Hello "
print(x +"world")
# here + is used for  adding variable and string

a="abc"
print(a*3)
# here * is used to multiply variable

print(x.upper())
print(x.lower())
# here .upper() is used  to set the whole variable ito upper case similarly .lower()
# is used to set the whole variable into lower case

x="Hello World" #you can alwasys reasiggn a variable
print(x.split())
# this creates alist of words in a variable
print(x.split("l")) #you can also assign a letter by which it gets splited or divided

#THE .FORMAT METHOD

print("my {}  ran away from {} to the {} looking for {}".format("dog","house","school","me"))
# here .format is used to format the string and put the values in the place of {}

print("The {0} {1} {2}".format("quick","brown","fox"))#you can also asign them as thier index
print("The {q} {b} {f}".format(b="brown",f="fox",q="quick"))
# you can also assign them as variables

x=92/33
print("the value of x is {x:2.3}".format(x=x))
# here 1 tells the the width of number and 3 tells accuracy of the number or how many digits after decimal point

# THE F-STRING METHOD
name="John"
age="21"
print(f"my name is {name} and I am {age} years old")
# here f-string is used to print the variable in the string
 
#  lists
mylist1=[1,2,3,4,5,6,7,8,9,100]
print(mylist1)
# here we created a list of numbers from 1 to 9 and 100
mylist1=[1,2,3,4,5,6,7,8,9,10]
print(mylist1)

# here we changed the 10th element of the list to 10
mylist1.append(11)
# adding a new elemnt to the list
print(mylist1)

poppeditem = mylist1.pop()#saving removed item
# removing the last element of the list
print(mylist1)
print(poppeditem)
# we can also pop item from a specific index by writing the index number in brackests
mylist1.pop(1)
print(mylist1)
# here we removed the 2nd element of the list

mylist2=[2,1,33,44,23,56,35,11,233,75,32,76,8,6]
mylist2.sort()
print(mylist2)
# here we sorted the list in ascending order
mylist3=[2,1,33,44,23,56,35,11,233,75,32,76,8,6]
# here we created another list
mylist3.sort()
print(mylist3)
# here we sorted the list in ascending order
print(mylist3.reverse())
# here we reversed the list
