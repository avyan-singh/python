def up_low(a):
    uppercasses=0
    lowercases=0
    for _ in a:
        if _.isupper():
            uppercasses+=1
        elif _.islower():
            lowercases+=1    
    return uppercasses,lowercases
print(up_low('Astig'))