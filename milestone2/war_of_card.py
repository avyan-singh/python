import random   
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Cards:
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        self.values=values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
mycard1=Cards('Two','Hearts')
mycard2=Cards('Three','Spades')
print(mycard1.values<mycard2.values)

class Deck:
    def __init__(self):
        self.All_cards=[]
        for rank in ranks:
            for suit in suits:
                Created_card=Cards(rank,suit)
                self.All_cards.append(Created_card)
    def __index__(self):
        random.shuffle(self.All_cards)
        mid = (len(self.All_cards) - 1) / 2
        player_1_deck=self.All_cards[:26]
        player_2_deck=self.All_cards[26:]
        return player_1_deck,player_2_deck

mydeck=Deck()
print(mydeck.All_cards[0])
deck1,deck2=mydeck.__index__()

class Player:
    def __init__(self,name):
        self.name=name
        self.All_card=[]

    def remmove_one(self):
        return self.All_card.pop(0)
        
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.All_card.extend(new_cards)
        else:
            self.All_card.append(new_cards)

    def __str__(self):
        return f"{self.name} have {len(self.All_card) } card"
 
new_player=Player('Jose')
print(new_player)
new_player.add_cards([mycard1,mycard2])
print(new_player)
print(new_player.All_card[0])
print(len(deck2))
print(len(deck1))

class Name:
    def __init__(self):
        self.Player1 = input("What's your name, Player 1? ")
        self.Player2 = input("What's your name, Player 2? ")

    def get_names(self):
        return self.Player1, self.Player2


myname = Name()
name1,name2=myname.get_names()
print(f"{name1}\n{name2}")

print(deck1[0].values)
print(deck1[0])
def start_game():
    name1, name2 = myname.get_names()
    
    print("Deck have been shuffled and assigned to you")
    a=0
    while deck1 and deck2:
        print(f"{name1} your card is {deck1[0]}")
        print(f"{name2} your card is {deck2[0]}")
        if deck1[a].values>deck2[a].values:
            deck1.append(deck2[0])
            deck2.pop(0)
            y=deck1.pop(0)
            deck1.append(y)
            print(f'{name1} has {len(deck1)} Cards and {name2} have {len(deck2)} cards \n{name1} won this round\n------------------------------------------------------------------------------')
        elif deck1[0].values<deck2[0].values:
            deck2.append(deck1[0])
            deck1.pop(0)
            x=deck2.pop(0)
            deck2.append(x)
            print(f'{name1} has {len(deck1)} Cards and {name2} have {len(deck2)} cards \n{name2} won this round\n------------------------------------------------------------------------------')
        elif deck1[0].values==deck2[0].values:
                deck1.pop(0)
                deck2.pop(0)
        if deck1==[]:
             print(f'{name2} won the game!')
        elif deck2==[]:
             print(f'{name1} won the game!')
        elif deck1==[] and deck2==[]:
            print("Draw nice game!")
tf=['YES' , 'NO']
start_staus=input('Do you want to start the game: ').upper()
while start_staus not in tf:
    start_staus=input('Do you want to start the game: ').upper()
if start_staus=='YES':
   start_game()
else:
    print("As you dont want to start the game .Game will not start.\nIn case of you wanting to play the game please run the code again")
    