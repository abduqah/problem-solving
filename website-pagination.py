def fetchItemsToDisplay(items, sortParameter, sortOrder, itemsPerPage, pageNumber):
  # Write your code here
  result = []
  sorting_vars = []
  real_ind = {}
  ind = 0

  for record in items:
    value = record[sortParameter]
    sorting_vars.append(value)
    real_ind[value] = ind
    ind += 1

  if sortOrder:
    sorting_vars = sorted(sorting_vars, reverse = True)
  else:
    sorting_vars = sorted(sorting_vars)

  start_point = itemsPerPage * pageNumber
  end_point = (itemsPerPage * pageNumber) + itemsPerPage

  if end_point > len(sorting_vars):
    end_point = len(sorting_vars)

  for _ in range(start_point, end_point):
    ind = real_ind[sorting_vars[_]]
    result.append(items[ind][0])

  return result

print(fetchItemsToDisplay([['owjevtkuyv', 58584272, 62930912], ['rpaqgbjxik', 9425650, 96088250], ['dfbkasyqcn', 37469674, 46363902],['vjrrisdfxe', 18666489, 88046739]], 2, 1, 2, 0))