def almost_there(a):
    if a >= 90 and 110 >= a:
        print(True)
        return True
    elif a>=190 and 210>=a:
        print(True)
        return True
    else:
        print(False)
        return False
        
almost_there(90) #--> True
almost_there(104)# --> True
almost_there(150) #--> False
almost_there(209)# --> True