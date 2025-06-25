def has_33(a):
    num4=len(a)-1
    num3=num4-1
    num2=1
    while not num3==-1:
         num2+=1
         num4=len(a)-num2
         num3=num4-1
         if a[num3]==a[num4]:
             return True
    return False
    

print(has_33([1,2,3,3,5]))

def has_33(a):
   i=0
   while not i==len(a)-1:
       if a[i]==3 and a[i+1]==3:
           return True
       i+=1
   return False
       

print(has_33([1,2,3,4,5]))