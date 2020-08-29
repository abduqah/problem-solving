def binary_gap(n):
  longest = []
  temp = []
  for _ in bin(n)[2:]:
    if _ == '1':
      if len(temp) > len(longest):
        longest = temp.copy()
        temp.clear()
    else:
      temp.append(_)

  print(len(longest))

binary_gap(20)
