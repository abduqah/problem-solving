a = int(input())
b = int(input())

def divmod(a, b):
  quotient = a//b
  remainder = a%b

  return tuple((quotient, remainder))

result = divmod(a, b)

print(result[0], result[1], result, sep='\n')
