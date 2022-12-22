def find_the_duplicate(nums):
    duplicate = set()
    find_duplicate = []
    for num in nums:
        if num in duplicate:
            find_duplicate.append(num)
        duplicate.add(num)
    return find_duplicate

print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))
print(find_the_duplicate([2, 1, 3, 4]))


    # """Find duplicate number in nums.

    # Given a list of nums with, at most, one duplicate, return the duplicate.
    # If there is no duplicate, return None

    #     >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
    #     1

    #     >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
    #     9

    #     >>> find_the_duplicate([2, 1, 3, 4]) is None
    #     True
    # """
