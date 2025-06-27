l1=[1,2,3,4,5,6]
print(l1)
l1.append(7)  # Append 7 to the end of the list
print(l1)
l1.pop(-1)  # Remove the last element (7)
print(l1)
l1.remove(6)  # Remove 6
print(l1)
print(l1.count(5))  # Count occurrences of 5
l2=range(6,11)  # Create a list with a range from 6 to 10
print(l2)
l1.extend(l2)  # Extend l1 with elements from l2
print(l1)
print(l1.index(10))  # Find the index of 10
l1.insert(0,0)  # Insert 0 at the beginning of the list
print(l1)
l1.reverse()  # Reverse the list
print(l1)
l1.sort()  # Sort the list in ascending order
print(l1)