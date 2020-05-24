def move_l_to_end(s,l,low,high):
  global final_s
  if low >= high:
    return
  current = s[low]
  if current != l:
    final_s += current
  move_l_to_end(s,l,low+1,high)
  if current == l:
    final_s += current
  return

s = 'strxixngxx'
l = 'x'
low = 0
high = len(s)
final_s = ''
move_l_to_end(s,l,low,high)
print(final_s)