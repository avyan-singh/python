def old_macdonald(name):
    named=''
    num2=0
    num3=len(name)-1
    while not num2>num3:
        if num2==0 or num2==3:
            named+=name[num2].upper()

        else:
            named+=name[num2]
        num2+=1
    print(named)
    return named
old_macdonald("macdonald")