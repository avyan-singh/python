mylist=[1,2,3,4,5]

nums= (_ for _ in mylist if _ > 3)

for _ in nums:
    print(_)

mylist=[1,2,3,4,5]

nums= [_ for _ in mylist if _ > 3]
print(nums)
# for _ in nums:
#     print(_)