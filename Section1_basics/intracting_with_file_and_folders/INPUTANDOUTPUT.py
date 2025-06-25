# INPUT AND OUTPUT
myfile1=open("myfile1.txt")
print(myfile1.read())   
print(myfile1.read())  
# the second time we call the read function it returns nothing because the foil pointer is at bottom of the file
myfile1.seek(0)
# this moves back the pointer to the start of th file
print(myfile1.read())
# so now we can read the file again
myfile1.seek(0)
print(myfile1.readlines())
# this reads the file line by line and returns a list of lines
myfile1.close()

with open("myfile1.txt") as mf1:
    print(mf1.read())
    print(mf1.readlines())

    
