def summer_69(*args):
    filtered_number=0
    for num in args:
        num=int(num)
        if num<6 or num>9:
         filtered_number=filtered_number+num
    return filtered_number
print(summer_69(1, 3, 5) )#--> 9
print(summer_69(4, 5, 6, 7, 8, 9))# --> 9
print(summer_69(2, 1, 6, 9, 11)) #--> 14