def multiply(a):
    num=1
    for _ in a:
        num*=_
    return num
print(multiply([1,2,3,-4]))