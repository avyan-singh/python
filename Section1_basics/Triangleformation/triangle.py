#   *  
#  ***
# *****
symbol="*"
till=15
default=0
nos=(till-1)//2
number2=1
while  default<till:
	space=" "*nos
	print(f"{space}{symbol*number2}")
	number2=number2+2
	symbol="*"
	nos=nos-1
	default+=1
	till=till-1


	

	