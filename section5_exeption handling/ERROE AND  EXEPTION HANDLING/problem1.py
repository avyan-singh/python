mylist=[input("First number: "),input("second number: "),input("Third  number: ")]

for i in mylist:
    try:
        i=int(i)
    
    except:
        print("That's not an integer")

    else:
        print(i ** 2)

