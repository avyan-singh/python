game_list=[1,2,3]
def dispay(game_list):
    print("Here is current list:")
    print(game_list)
def ask_input():
    num_list=[0,1,2]
    string1=input("Tell what string you want to replace: ")
    num=input('Which index position you want to change(0,1 or 2): ')
    if int(num) not in num_list:
        num=input('Which index position you want to change(0,1 or 2): ')
    else:
        num=int(num)
        game_list[num]=string1
        print(game_list)
        print("your current list is given as above")
def continuing_code():
    ask_input()
    Y_or_N=input("Do you want to continue the game(Y or N): ")
    YN=['Y','N']
    while Y_or_N not in YN:
        if Y_or_N not in YN:
            print("I don't understand please tell")
            Y_or_N=input("Do you want to continue the game(Y or N): ")
    if Y_or_N=='Y':
        ask_input()
    else:
        print('Thank you for playing')
continuing_code()
