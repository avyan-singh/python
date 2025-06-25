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
    def return_deck(self):
        random.shuffle(self.All_cards)
        return self.All_cards

mydeck=Deck()
print(mydeck.All_cards[0])

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
deck=mydeck.return_deck()
print(deck[0])
