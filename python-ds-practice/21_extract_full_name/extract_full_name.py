def extract_full_names(people):
   
    return f"{people['first']} {people['last']}"

names = [{'first': 'Ada', 'last': 'Lovelace'},{'first': 'Grace', 'last': 'Hopper'}, ]
print("Full Name:",extract_full_names(names))
 

#print("Full Name:",extract_full_names(names))

    # """Return list of names, extracting from first+last keys in people dicts.

    # - people: list of dictionaries, each with 'first' and 'last' keys for
    #           first and last names

    # Returns list of space-separated first and last names.

    #     >>> 

    #     >>> extract_full_names(names)
    #     ['Ada Lovelace', 'Grace Hopper']
    # """