def capitalize(phrase):
    
    
    phrase = phrase[:1:].upper() + phrase[1::]
    return phrase

print("Capitalized first letter of phrase:",capitalize('python'))
print("Capitalized first letter of phrase:",capitalize('only first word'))
  