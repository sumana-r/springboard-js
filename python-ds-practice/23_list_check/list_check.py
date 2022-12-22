def list_check(lst):
    for sublist in lst:
        if not isinstance(sublist, list):
            return False
    return True

print("check list", list_check([[1], [2, 3]]))
print("check list", list_check([[1], "nope"]))
    # """Are all items in lst a list?

    #     >>> list_check([[1], [2, 3]])
    #     True

    #     >>> list_check([[1], "nope"])
    #     False
    # """
