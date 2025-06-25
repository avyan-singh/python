def ask():
    while True:
        num = input("Type number you want square of: ")
        
        try:
            num = int(num)

        except:
            print("That's not an integer")

        else:
            print(num**2)
            break


ask()
