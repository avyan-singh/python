number=(input("which number's table you want:"))
if number.isdigit():
    number=int(number)
    till=10
    start=1
    while not start>till:
        print(number*start)
        start=start+1
else:
        print("PLEASE ENTER A VALID NUMBER")