def numberOfTokens(expiryLimit, commands):
  # Write your code here
  result = []
  tokens = {}

  for _ in commands:
    try:
      token_data = tokens[_[1]]

      if token_data['valid']:
        if can_reset(token_data['exp'], _[2]):
          print(tokens)
          token_data['exp'] = _[2] + expiryLimit
        else:
          token_data['exp'] = _[2]
          token_data['valid'] = False
    except:
      if _[0] == 0:
        tokens[_[1]] = {'created': _[2], 'valid': True, 'exp': _[2] + expiryLimit}
  last_t = commands[-1][2]
          
  for k, _ in tokens.items():
    if _['valid'] and _['exp'] >= last_t:
      result.append(k)

  return len(result)

def can_reset(exp, current_t):
  return exp >= current_t

print(numberOfTokens(3, [[1, 23937, 405],
[1, 2755, 643],
[0, 21230, 1474],
[1, 21230, 1609],
[0, 24942, 2453],
[0, 15143, 2839],
[0, 18242, 3321],
[1, 24942, 3709],
[0, 6123, 4310],
[1, 18242, 5031],
[0, 17229, 5532],
[0, 721, 6456],
[0, 778, 6973],
[0, 1249, 7200],
[0, 18124, 7623],
[0, 31978, 8477],
[0, 25030, 9124],
[0, 24137, 9759],
[1, 18242, 9784],
[1, 1249 ,9903],
[1, 24942, 10508],
[0, 18013, 10696],
[1, 4419 ,11688],
[0, 3560 ,12153],
[1, 18124, 12252],
[0, 26340, 12399],
[0, 18550, 12588],
[0, 25135, 13007],
[0, 31659, 13583],
[1, 24137, 13960],
[1, 31659, 14955],
[1, 4217 ,15438],
[1, 778 ,15651],
[0, 21632, 16572],
[1, 24942, 16979],
[1, 25135, 17894],
[0, 16985, 18501],
[0, 17091, 18690],
[0, 24105, 19563],
[1, 31659, 20361],
[0, 15160, 20868],
[1, 18013, 21365],
[0, 23900, 22236],
[1, 19466, 22758],
[1, 721 ,23560],
[0, 16542, 23864],
[0, 5852, 24281]]))