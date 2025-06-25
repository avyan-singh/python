def greaterthan(a,b):
    if a>b:
        print(b)
    elif b>a:
        print(a)
    else:
        print ("b=a")
def smallerthan(a,b):
    if a>b:
        print(a)
    elif b>a:
        print(b)
    else:
        print ("b=a")
def myfunc(a,b):
    if a % 2==0 and b % 2 == 0:
        greaterthan(a,b)
    else:
        smallerthan(a,b)
        

myfunc(2,4)