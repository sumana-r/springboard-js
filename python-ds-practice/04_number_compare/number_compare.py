def number_compare(a, b):
    if a > b:
        return f"{a} is greater {b}"
    elif a < b:
        return f"{b} is greater {a}"
    elif a == b:
        return "Numbers are equal"
    else:
        return "None"

print("The given number:", number_compare(1, 1))
print("The given number:", number_compare(-1, 1))
print("The given number:", number_compare(1, -2))
