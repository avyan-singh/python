# def myfunc():
#     print( 'My code')

def decorator(func):
    print('exta code')
    func()
    print('exta code')

# decorator(myfunc)

@decorator
def myfunc():
    print( 'My code')
