set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
l1=set1.intersection(set2)
for i in set1.union(set2):
    if i not in l1:
        print(i)
   