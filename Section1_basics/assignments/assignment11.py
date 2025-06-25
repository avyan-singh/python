def eleven_number(a,b,c):
    Total=a+b+c
    if (a==11 or b==11 or c==11) and Total>21:
        Total-=10
    return Total
def blackjack(a,b,c):
   Total=eleven_number(a,b,c)
   return Total if Total<=21 else "Bust"
print(blackjack(5,6,7))# --> 18
print(blackjack(9,9,9)) #--> 'BUST'
print(blackjack(9,9,11)) #--> 19