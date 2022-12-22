def compact(lst):
    truelist = [truelist for truelist in lst if truelist]
    return truelist

print("the true elements are", compact([0, 1, 2, '', [], False, (), None, 'All done']))
  