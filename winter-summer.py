# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(T):
  # write your code in Python 3.6
  max_summer = max(T)
  winter = [T[0]]
  max_winter = T[0]
  temp_summer = []
  
  T.remove(T[0])
  for t in T:
    if t < max_winter:
      if len(temp_summer) > 0:
        max_winter = max(temp_summer)
        winter.extend(temp_summer)
        winter.append(t)
        temp_summer.clear
      else:
        winter.append(t)
    elif t == max_summer:
      break
    else:
      temp_summer.append(t)

  print(len(winter))
  pass

solution( [5, -2, 3, 8, 6])