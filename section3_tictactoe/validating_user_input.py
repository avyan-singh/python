def display(r1,r2,r3):
    symbols=['X','O']
    symbol=input("which symbol you want to be X or O: ").upper()
    while symbol not in symbols:   
         symbol=input("which symbol you want to be X or O: ") 
    data=(f"{r1}\n{r2}\n{r3}")
    print (f"{r1}\n{r2}\n{r3}")
    print("give the data as row first and then  column")
    user_inputrow=input("please enter the row number(from 1 to 3): ")
    user_inputcolumn=input("please enter the column number(from 1 to 3): ")
    valid_range=[1,2,3]
    if user_inputrow.isdigit():
        user_inputrow=int(user_inputrow)
        if user_inputrow in valid_range:
            row=int(user_inputrow)
        else:
            print("please enter a number in range of 1 to 3 for row number")
    else:
         print("please enter a digit")
    if user_inputcolumn.isdigit():
                user_inputcolumn=int(user_inputcolumn)
                if user_inputcolumn in valid_range:
                    column=int(user_inputcolumn)
                else:
                    print("please enter a number in range of 1 to 3 for column number")
    else:
         print('please enter a digit')
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
display_=display(row1,row2,row3)#here we diplay a tic tac toe looking like board


