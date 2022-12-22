def flip_case(phrase, to_swap):
    swapped_str = ""
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            letter = letter.swapcase()
        swapped_str += letter    
    return swapped_str

print("Flip [to_swap] case is:",flip_case('Aaaahhh', 'a'))
print("Flip [to_swap] case is:",flip_case('Aaaahhh', 'A'))
print("Flip [to_swap] case is:",flip_case('Aaaahhh', 'h'))
   
