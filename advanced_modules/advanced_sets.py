myset=set()
myset.add(1)
myset.add(2)
myset.add(3)#add elements to the set
sc=myset.copy()#copy the set
print(sc)
myset.add(3)#adding duplicate element, it will not be added again
print(myset)
myset.remove(2)#remove element from the set
print(myset)
myset.discard(3)#discard element from the set, it will not raise error if element is not present
print(myset)
myset.clear()#clear the set
print(myset)
myset={1,2,3,4}
print(myset.difference(sc))#difference between two sets
myset.difference_update(sc)#update the set with the difference
print(myset)
s1={1,2,3,4}
s2={1,2,3,5}
s3={5,6,7,8}
print(s1.intersection(s2))#intersection of two sets
s1.intersection_update(s2)#update the set with the intersection
print(s1)
print(s1.isdisjoint(s2))#intersection of multiple sets
print(s1.isdisjoint(s3))#intersection of multiple sets
s1={1,2,3,4}
s2={1,2}
print(s2.issubset(s1))#check if s1 is subset of s2
print(s1.issuperset(s2))#check if s1 is superset of s2
print(s2.symmetric_difference(s1))#symmetric difference of two sets
print(s1.union(s3))#union of two sets
s1.update(s3)#update the set with the union
print(s1)