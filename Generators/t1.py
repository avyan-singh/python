def squares(num):
    for _ in range(1,num+1):
        yield _**2
# def squares(num):
#   yield num**2
# print(squares(10))

# for _ in squares(range(1,11)):
#     print(_)
def squares(num):
    yield num ** 2

for _ in range(1,11):
    print(squares(_))