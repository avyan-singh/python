def display(r1,r2,r3):
    print (f"{r1}\n{r2}\n{r3}")
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
display_=display(row1,row2,row3)#here we diplay a tic tac toe looking like board
print("give the data as row first and then  column")
user_inputrow=input("please enter the numbers: ")
user_inputcolumn=input("please enter the numbers: ")
row=int(user_inputrow)
column=int(user_inputcolumn)
row=row-1