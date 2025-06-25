from collections import Counter
l1=[1,2,3,3,3,3,3,2,2,2,1,1,1,1,6,7,7,8,7,654,5,7,7,7,7,6,6,7]
c=Counter(l1)
print(c.most_common(3))

from collections import defaultdict
d1=defaultdict(lambda:10)
d1['a']=100
print(d1['a'])
print(d1['y'])

from collections import namedtuple

dog=namedtuple('dog',['name','breed','color'])
d=dog('sam','husky','red')
print(d.breed)
print(d.name)
print(d.color)
