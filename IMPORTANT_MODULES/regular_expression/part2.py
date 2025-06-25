import re
text='My number is 111-222-3333 and his is 444-555-6666'
phonenumber=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phonenumber)#it will only print starting one
phonenumber=re.findall(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phonenumber)#it will print all

phonenumber=re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phonenumber)
phonenumber=re.findall(r'\d{3}-\d{3}-\d{4}',text)
print(phonenumber)

phone_number=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phonenumber1=re.search(phone_number,text)
print(phonenumber1.group())