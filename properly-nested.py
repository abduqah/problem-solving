def solution(S):
  temp = []
  last_value = S[0]

  if len(S) % 2 == 0:
    for _ in S:
      if invers(last_value, _):
        temp.pop()
        if (len(temp) > 0): last_value = temp[-1]
      else:
        temp.append(_)
        last_value = _
        pass

    print (0 if len(temp) > 0 else 1)
  else:
    print(0)


def invers(last_v, new_v):
  inv = {'(': ')', '{': '}', '[': ']'}
  try:
    return inv[last_v] == new_v
  except:
    return False


solution("([)()]")