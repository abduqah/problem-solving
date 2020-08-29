def solution(A):
  last_sum = sum(A)
  new_arr = remove_max(A)
  new_sum = sum(new_arr)
  while new_sum < last_sum:
    if new_arr:
      new_arr = remove_max(new_arr)
      last_sum = new_sum
      new_sum = sum(new_arr)
    else:
      break

  print(last_sum)
  pass

def remove_max(arr):
  m = max(arr)
  temp = m
  arr.remove(m)
  for i in reversed(range(m)):
    if i > temp: continue
    if i in arr :
      temp -= i
      arr.remove(i)

  if temp > 0:
    arr.append(temp)

  return arr


solution([1,5,2,-2])