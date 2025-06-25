# def squares(num):
#     list1=[]
#     for _ in range(1,num+1):
#         list1.append(_**2)
#     return list1
# myfunc=squares
# print(myfunc(10))

def squares(num):    
    for _ in range(1,num+1):
        print(f"number is {_}")
        yield _
        # return _
print(squares(10))
# print(list(squares(10)))
# myfunc=squares(10)
# print(squares(10))
 
# for _ in squares(10):
#     print(f"outer loop {_}")
#     print(_)

# mystring="World"

# mystring_iter=iter(mystring)

# print(next(mystring_iter))
# print(next(mystring_iter))
# print(next(mystring_iter))
# print(next(mystring_iter))
# print(next(mystring_iter))
# print(next(mystring_iter))

# for _ in mystring_iter:
#     print(list(_))


