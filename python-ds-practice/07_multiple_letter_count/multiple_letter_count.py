def multiple_letter_count(phrase):
    my_dict = {}
    for letter in phrase:
        count = [char for char in phrase if char == letter]
        my_dict[letter] = len(count)
    return my_dict

print("Letter count:", multiple_letter_count('yay'))
print("Letter count:", multiple_letter_count('Yay'))
   