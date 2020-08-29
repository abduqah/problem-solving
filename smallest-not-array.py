
def solution(A):
  # write your code in Python 3.6
  sorted_arr = sorted(set(A))
  m = max(sorted_arr)
  minm = min(sorted_arr)
  if 1 not in sorted_arr:
    return 1
  elif m == len(sorted_arr) and minm > 0:
    return m + 1
  else:
    minm = max([1, minm])
    for i in range(minm, m):
      if (i not in sorted_arr): return i


print(solution([1,2,3]))