def multiply_even_numbers(nums):
    prod = 1
    for num in nums:
        if num % 2 == 0:
            prod = prod * num
    return prod
  
     
        


print("multiplied even number is:", multiply_even_numbers([2, 3, 4, 5, 6]))
print("multiplied even number is:", multiply_even_numbers([3, 4, 5]))
print("multiplied even number is:", multiply_even_numbers([1, 3, 5]))
