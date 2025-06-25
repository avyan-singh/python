def masteryoda(a):
    string1=" " 
    x=a.split()
    num1=len(x)-1
    num2=0
    while not num1==num2:
        string1+=x[num1]
        string1+=' '
        num1-=1
    return string1

   
print(masteryoda("hi how are you"))