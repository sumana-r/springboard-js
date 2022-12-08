def print_upper_words(words):
    for word in words:
        print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper2_words(words, must_start_with):
    for word in words:
        for start in must_start_with:
            if word.startswith(start):
                print(word.upper())

print_upper2_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

# print word starts with the letter 'e'
def print_upper1_words(words):
    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())


print_upper1_words(["EAGLE","HAND","EAR","LARGE","EGG"])
