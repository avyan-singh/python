
def prime_number(a):
    if a<2:
        return 0
    x=2
    primenumbers=[]
    while not x>a:
        for y in range(2,x):
            if x%y==0:
                break
        else:
            primenumbers.append(x)
        x+=1
    print(primenumbers)
    return len(primenumbers)
       
print(prime_number(100))
       
def primenumber(a):
    if a<2:
       return 0
    x=2
    primenumbers=[]
    while not x>a:
        for y in range(2,x):
            if x % y == 0:
                break
        else:
            primenumbers.append(x)
        x+=1
    print(primenumbers)
    return len(primenumbers)

print(primenumber(10000))








    
    


