number=68
default=0
num=number+1
factorial=1
while not number==default:
	factorial=factorial*(num-1)
	num-=1
	default+=1
	
print(factorial)
