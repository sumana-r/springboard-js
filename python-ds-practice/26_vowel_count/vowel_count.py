def vowel_count(phrase):
    phrase = phrase.lower()
    count = {}
    vowels = "aeiou"
    for letter in phrase:
        if letter in vowels:
            count[letter] = count.get(letter, 0) + 1
    return count

print("vowels count:", vowel_count('rithm school'))
print("vowels count:", vowel_count('HOW ARE YOU? i am great!') )
    # """Return frequency map of vowels, case-insensitive.

    #     >>> vowel_count('rithm school')
    #     {'i': 1, 'o': 2}
        
    #     >>> vowel_count('HOW ARE YOU? i am great!') 
    #     {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    # """