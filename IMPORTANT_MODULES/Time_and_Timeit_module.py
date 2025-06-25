import time
def func_one(num):
    return list(map(str,range(1,num+1)))
def func_two(num):
    return [str(num) for num in range(1, num+1)]
sttime1=time.time()
func_one(10000)
endtime1=time.time()
sttime2=time.time()
func_two(10000)
endtime2=time.time()
elapsedtime1=endtime1-sttime1
elapsedtime2=endtime2-sttime2
print(elapsedtime1,elapsedtime2)
import timeit
stmt1="""
func_one(1)
"""
setup1='''
def func_one(num):
    return list(map(str,range(1,num+1)))
'''
stmt2='''
func_two(1)
'''
setup2='''
def func_two(num):
    return [str(num) for num in range(1, num+1)]
'''
print(timeit.timeit(stmt1,setup1,number=10000000))

print(timeit.timeit(stmt2,setup2,number=10000000))