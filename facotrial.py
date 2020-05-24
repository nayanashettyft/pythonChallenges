def memoized_factorial(n):
  global cache
  if cache[n]:
    return cache[n]
  if n == 0:
    cache[n] = 0
  elif n == 1:
    cache[n] = 1
  else:
    cache[n] = memoized_factorial(n-1) + memoized_factorial(n-2)
  return cache[n]

def down_up_factorial(n):
  global cache
  for i in range(n+1):
    if i == 0:
      a = 0
    elif i == 1:
      b = 1
    else:
      a,b = b,a + b
  return b

n = 5
cache = [0]*(n+1)
# print(memoized_factorial(n))
print(down_up_factorial(n))