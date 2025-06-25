def display_board(board):
    Board= (f"{board[0]}|{board[1]}|{board[2]}\n{board[3]}|{board[4]}|{board[5]}\n{board[6]}|{board[7]}|{board[8]}")
    
    return Board

def talk_to_user():
    YN=['YES','NO']
    Y_N=input("Player1:Do you want to start the game(Yes or No): ").upper()
    while Y_N not in YN:
        if Y_N not in YN:
            Y_N=input("Player1:Do you want to start the game(Yes or No): ").upper()
    if Y_N=='YES':
        return True
    else:
        return False

def symbol_assignment():
    if talk_to_user()==True:
        symbols=['X','O']
        symbol1=input("Player1:Which symbol you want to be(X or O): ").upper()
        while symbol1 not in symbols:
            if symbol1 not in symbols:
                symbol1=input("Player1:Which symbol you want to be(X or O): ").upper()
                print('sorry invalid symbol!!!')
        if symbol1=='X':
            symbol2='O'
            print('Player2:You have been assigned as O')
        else:
            symbol2='X'
            print('Player2:You have been assigned as X')
        return symbol1,symbol2

def in_range(ranged, count, place,mylist):
    count += 1
    if count%2 == 0:
        while place not in ranged:
            if place not in ranged:
                place=input(f'Player1:Choose number from:{mylist} ')
                print('please print a valid number within given range')
        return place
    else:
        while place not in ranged:
            if place not in ranged:
                place=input(f'Player2:Choose number from:{mylist} ')
                print('please print a valid number within given range')
        return place

def add_to_board():
        mylist=[0,1,2,3,4,5,6,7,8]
        count = 0
        symbol1, symbol2 = symbol_assignment()
        ranged=[0,1,2,3,4,5,6,7,8,9]
        print(display_board(ranged))
        inputs=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        user_input(ranged, count, inputs, symbol1, symbol2,mylist)
            
        

def user_input(ranged, count, inputs, symbol1, symbol2,mylist):
    wongame=False
    while count<9:
        if count==9 and wongame!=True:
            print('DRAW')
        if wongame==True:    
            break 
        else:
            if(count%2==0):
                place=int(input(f'player 1: choose number from:{mylist} '))
                in_range(ranged, count, place,mylist)
                mylist.remove(place)
                if inputs[place] == ' ':
                    inputs[place]=symbol1
                    print(display_board(inputs))
                else:
                    while inputs[place]!=' ':
                        place=int(input(f'Player1:Choose number from:{mylist} '))
                        mylist.remove(place)
                        in_range(ranged, count, place,mylist)
                    print(display_board(inputs)) 
                    mylist.remove(place)            
                inputs[place]=symbol1
                if inputs[0]==inputs[1]==inputs[2]==symbol1 or inputs[3]==inputs[4]==inputs[5]==symbol1 or inputs[6]==inputs[7]==inputs[8]==symbol1 or inputs[0]==inputs[3]==inputs[6]==symbol1 or inputs[1]==inputs[4]==inputs[7]==symbol1 or inputs[2]==inputs[5]==inputs[8]==symbol1 or inputs[0]==inputs[4]==inputs[8]==symbol1 or inputs[2]==inputs[4]==inputs[6]==symbol1:
                    print('Congratulations you won the game')
                    wongame=True
            else:
                while inputs[place]!=' ':
                    place=int(input(f'Player2:choose number from:{mylist} '))
                    in_range(ranged, count, place,mylist)
                mylist.remove(place)
                if inputs[place]==' ':
                    inputs[place]=symbol2
                    print(display_board(inputs))
                else:
                    while inputs[place]!=' ':
                        place=int(input(f'Player2:Choose number from:{mylist} '))
                        in_range(ranged, count, place,mylist)
                mylist.remove(place)
                if inputs[0]==inputs[1]==inputs[2]==symbol2 or inputs[3]==inputs[4]==inputs[5]==symbol2 or inputs[6]==inputs[7]==inputs[8]==symbol2 or inputs[0]==inputs[3]==inputs[6]==symbol2 or inputs[1]==inputs[4]==inputs[7]==symbol2 or inputs[2]==inputs[5]==inputs[8]==symbol2 or inputs[0]==inputs[4]==inputs[8]==symbol2 or inputs[2]==inputs[4]==inputs[6]==symbol2:
                    print('Congratulations you won the game')
                    wongame=True
            count+=1
add_to_board()