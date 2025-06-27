d={'k1':1,"k2":2}#create a dictionary
print(d)
d2={x:x**2 for x in range(1,11)}#create a dictionary using dictionary comprehension
print(d2)
d3={k:v for k,v in zip(['k1','k2'],range(1,3))}#create a dictionary using zip function
print(d3)
for i in d.items():
    print(i)
