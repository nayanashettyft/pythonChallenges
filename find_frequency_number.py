def find_freq_number(arr,x):
  high = len(arr) - 1
  low = 0
  start_index = find_start_index(arr, low, high, x)
  end_index = find_end_index(arr,low,high,x)
  return end_index - start_index + 1
    
def find_start_index(arr, low, high, x):
  if high >= low:
    mid = (high + low) // 2
    if (mid == 0 or arr[mid-1] < x) and arr[mid] == x:
      return mid
    else:
      if arr[mid] < x:
        return find_start_index(arr,mid+1,high,x)
      else:
        return find_start_index(arr,low,mid-1,x)
  return -1

def find_end_index(arr, low, high, x):
  if high >= low:
    mid = (high + low) // 2
    if (mid == len(arr) - 1  or arr[mid+1] > x) and arr[mid] == x:
      return mid
    else:
      if arr[mid] > x:
        return find_end_index(arr,low,mid-1,x)
      else:
        return find_end_index(arr,mid+1,high,x)
  return -1


inp = list(map(int, input('enter a list of numbers: ').split()))
number_to_count = int(input('enter the number to be counted in the array: '))
while inp and number_to_count:
  print("min freq largest number is", find_freq_number(inp,number_to_count))
  inp = list(map(int, input("enter a list of numbers: ").split()))
  number_to_count = int(input('enter the number to be counted in the array: '))