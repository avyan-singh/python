def table():
    a=int(input("Enter a number: "))
    start=1
    stop=10
    if a.isdigit():
        a=int(a)
        while not  start>stop:
            print(a*start)
            start=start+1
    else:
        print("Please enter a valid number.")

table()