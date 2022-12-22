def frequency(lst, search_term):
    fre_value = [val for val in lst if val == search_term]
    return len(fre_value)
    
print("Return frequency of term in lst is", frequency([1, 4, 3, 4, 4], 4))
print("Return frequency of term in lst is", frequency([1, 4, 3], 7))
   