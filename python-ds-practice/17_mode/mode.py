def mode(nums):
    num = max(set(nums), key = nums.count)
    return num

print("highest frequency:", mode([1, 2, 1]))
print("highest frequency:", mode([2, 2, 3, 3, 2]))

