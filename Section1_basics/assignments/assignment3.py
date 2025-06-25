def animal_crackers(x):
    a,b=x.split()
    if a[0]==b[0]:
        print(True)
    else:
        print(False)

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')