import re
text='My dog is very nutorious'
print(re.search(r'cat|dog'.upper(),text.upper()))#here | stands for OR.

text='This   is his disc'
print(re.findall(r'is',text))
print(re.findall(r'.is',text))#Here adding . will give entire word not just the string you have given.

print(re.findall(r'^\d','2 is a number'))#check if  the string start with an integer
print(re.findall(r'^\d',' is 2 a number'))

print(re.findall(r'\d$','the number is 1'))#check if  the string end with an integer
print(re.findall(r'\d$',' is 2 a number'))

a=re.findall(r'[^\d]+','There are 6 number inside 75 me 88')
print(a)
print(' '.join(a))
