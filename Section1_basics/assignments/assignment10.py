def eleven_number(a,b,c):
    Total=a+b+c
    if (a==11 or b==11 or c==11) and Total>21:
        Total-=10
    return Total