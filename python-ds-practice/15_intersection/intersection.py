def intersection(l1, l2):
    return list(set(l1) & set(l2))
print("intersection of two lists:", intersection([1, 2, 3], [2, 3, 4]))
print("intersection of two lists:", intersection([1, 2, 3], [1, 2, 3, 4]))
print("intersection of two lists:", intersection([1, 2, 3], [3, 4]))
print("intersection of two lists:", intersection([1, 2, 3], [4, 5, 6]))

