def spy_game(nums):
    i=0
    sequence=[0,0,7]
    for num in nums:
        if sequence[i]==num:
            sequence.pop(0)
            if not sequence:
                return True
    return False

print(spy_game([1,2,4,0,0,7,5])) #--> True
print(spy_game([1,0,2,4,0,5,7])) #--> True
print(spy_game([1,7,2,0,4,5,0])) #--> False
    