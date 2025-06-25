def makes_twenty(a,b):
    if a+b==20:
        print(True)
    elif a==20 or b==20:
        print(True)
    else:
        print(False)

makes_twenty(20,10) #--> True
makes_twenty(12,8)# --> True
makes_twenty(2,3) #--> False