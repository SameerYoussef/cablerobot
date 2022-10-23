import math

'''
Spreads a [short]er number (representing a number of indicies in a list)
fairly equals across a [long]er number

e.g. spread(5, 2) -> [False, True, False, True, False]

Where count(True) == [short] and count(True) + count(False) == [long]
'''

def spread(long, short):
  if short == 0:
    return [False] * long
  if long == 1 and short == 1:
    return [True]
  
  if long % 2 == 0:
    left = right = int(long / 2)
    if short == 1:
      return [False] * (left - 1) + [True] + [False] * right # default to fewer lefts if even
    elif short % 2 == 0:
      short = int(short / 2)
      return spread(left, short) + spread(right, short)
    else:
      short = math.floor(short / 2)
      return spread(left - 1, short) + [True] + spread(right, short) # default to fewer lefts if even
  else:
    left = right = math.floor(long / 2)
    if short == 1:
      return [False] * left + [True] + [False] * right
    elif short % 2 == 0:
      short = int(short / 2)
      return spread(left, short) + [False] + spread(right, short)
    else:
      short = math.floor(short / 2)
      return spread(left, short) + [True] + spread(right, short)

def evenize(all_steps):
  
  longest = max(all_steps)
  
  def transform(x, type):
    if x:
      return type
    else:
      return ''

  result_a = map(transform, spread(longest, all_steps[0]), longest * 'a')
  result_b = map(transform, spread(longest, all_steps[1]), longest * 'b')
  result_c = map(transform, spread(longest, all_steps[2]), longest * 'c')
  result_d = map(transform, spread(longest, all_steps[3]), longest * 'd')

  def convertTuple(tup):
      st = ''.join(map(str, tup))
      return st

  return list(map(convertTuple, zip(result_a, result_b, result_c, result_d)))

if __name__ == "__main__":
  print(evenize([0, 0, 0, 0]))
