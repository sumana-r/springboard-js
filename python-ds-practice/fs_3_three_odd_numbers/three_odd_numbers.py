def three_odd_numbers(nums):
    sum = 0
    count = 0
    for i in range(len(nums)):
      if(nums[i] % 2 != 0) & (count <= 3):
        sum += nums[i]
        count += 1
    return sum % 2 != 0
            
     

print(three_odd_numbers([1, 2, 3, 4, 5]))
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))
print(three_odd_numbers([5, 2, 1]))
print(three_odd_numbers([1, 2, 3, 3, 2]))

    # """Is the sum of any 3 sequential numbers odd?"

    #     >>> three_odd_numbers([1, 2, 3, 4, 5])
    #     True

    #     >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
    #     True

    #     >>> three_odd_numbers([5, 2, 1])
    #     False

    #     >>> three_odd_numbers([1, 2, 3, 3, 2])
    #     False
    # """
