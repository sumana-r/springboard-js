from functools import reduce
def find_factors(num):
    return set(reduce(list.__add__,([i,num//i] for i in range(1, int(num**0.5) + 1) if num % i == 0)))

print("the factor number is ", find_factors(10))
print("the factor number is ", find_factors(11))
print("the factor number is ", find_factors(111))
print("the factor number is ", find_factors(321421))

    # """Find factors of num, in increasing order.

    # >>> find_factors(10)
    # [1, 2, 5, 10]

    # >>> find_factors(11)
    # [1, 11]

    # >>> find_factors(111)
    # [1, 3, 37, 111]

    # >>> find_factors(321421)
    # [1, 293, 1097, 321421]
    # """
