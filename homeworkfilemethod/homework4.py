def unique_list(a):
    mylist=[]
    for _ in a:  
        if _ not in mylist:
            mylist.append(_)
    return mylist
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))