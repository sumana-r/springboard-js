def same_frequency(num1, num2):
    count1 = {}
    count2 = {}
    for n in str(num1):
        count1[n] = count1.get(n, 0) + 1
    
    for n2 in str(num2):
        count2[n2] = count2.get(n2,0) + 1

    return count2 == count1

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))
    
    
    # """Do these nums have same frequencies of digits?
    
    #     >>> same_frequency(551122, 221515)
    #     True
        
    #     >>> same_frequency(321142, 3212215)
    #     False
        
    #     >>> same_frequency(1212, 2211)
    #     True
    # """