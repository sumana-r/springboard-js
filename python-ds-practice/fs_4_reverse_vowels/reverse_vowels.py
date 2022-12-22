def reverse_vowels(s):
    vowel_lst =[]
    vowels = "aeiouAEIOU"
    word_list = list(s)
    for char in s:
        if char in vowels:
            vowel_lst.append(char)
    vowel_lst = vowel_lst[::-1]
    j = 0
    for i in range(len(word_list)):
        if word_list[i] in vowels:
            word_list[i] = vowel_lst[j]
            j += 1
    return "".join(word_list)

print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))

    # """Reverse vowels in a string.

    # Characters which re not vowels do not change position in string, but all
    # vowels (y is not a vowel), should reverse their order.

    # >>> reverse_vowels("Hello!")
    # 'Holle!'

    # >>> reverse_vowels("Tomatoes")
    # 'Temotaos'

    # >>> reverse_vowels("Reverse Vowels In A String")
    # 'RivArsI Vewols en e Streng'

    # reverse_vowels("aeiou")
    # 'uoiea'

    # reverse_vowels("why try, shy fly?")
    # 'why try, shy fly?''
    # """