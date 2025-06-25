import random


def rand_num(low,high,n):
    for _ in range(1,n+1):
        yield random.randint(low,high)


for num in rand_num(1,10,12):
    print(num)