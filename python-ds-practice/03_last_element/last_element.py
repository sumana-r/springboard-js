def last_element(lst):
    if len(lst) == 0:
        return "None"
    else:
        return lst[-1]
   

print("The Last Element is", last_element([1, 2, 3]))
print("The Last Element is", last_element([]))