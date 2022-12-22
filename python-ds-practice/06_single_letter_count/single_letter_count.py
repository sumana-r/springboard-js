def single_letter_count(word, letter):
    
    count = [char for char in word if char.lower() == letter]
    print(count)
    return len(count)

print("How many times does letter appear in word:", single_letter_count('Hello World', 'h'))
print("How many times does letter appear in word:", single_letter_count('Hello World', 'z'))
print("How many times does letter appear in word:", single_letter_count("Hello World", 'l'))
