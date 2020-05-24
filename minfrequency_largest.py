def min_frequency_largest(arr):
  d = {}
  # generate frequency of each element in the arrary
  for n in arr:
    if d.get(n):
      d[n] += 1
    else:
      d[n] = 1
  # find the minimum frequency value
  min_freq = min(d.values())
  # construct an array with from hash with min frquency and sort it.
  # last element iin this array iis the largest
  arr_min_freq_num = [key for key in d if d[key] == min_freq]
  arr_min_freq_num.sort()
  return arr_min_freq_num[-1]

inp = list(map(int, input("enter a list of numbers: ").split()))
while inp:
  print("min freq largest number is", min_frequency_largest(inp))
  inp = list(map(int, input("enter a list of numbers: ").split()))