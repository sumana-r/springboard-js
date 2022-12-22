def is_palindrome(phrase):
    
     return phrase.replace(" ", "").lower() == phrase.replace(" ", "")[::-1].lower()  


print("Is phrase a palindrome?", is_palindrome('tacocat'))
print("Is phrase a palindrome?", is_palindrome('noon'))
print("Is phrase a palindrome?", is_palindrome('robert'))
print("Is phrase a palindrome?", is_palindrome('taco cat'))
print("Is phrase a palindrome?", is_palindrome('Noon'))

    # """Is phrase a palindrome?

    # Return True/False if phrase is a palindrome (same read backwards and
    # forwards).

    #     >>> is_palindrome('tacocat')
    #     True

    #     >>> is_palindrome('noon')
    #     True

    #     >>> is_palindrome('robert')
    #     False

    # Should ignore capitalization/spaces when deciding:

    #     >>> is_palindrome('taco cat')
    #     True

    #     >>> is_palindrome('Noon')
    #     True
    # """
