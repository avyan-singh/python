x =input("Value of x should be: ")
y = input("Value of y should be: ")

try:
    x=int(x)
    y=int(y)
    z = x/y
    
except ValueError:
    print("That's not an integer")

except ZeroDivisionError:
    print('Denominator ie. y cannot be zero')

else:
    print(z)