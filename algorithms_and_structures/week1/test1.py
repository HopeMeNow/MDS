def find_numbers(a, k):
  left, right = 0, len(a) - 1
  while left < right:
    summ = a[left] + a[right]
    if summ > 10:
      right -= 1
    elif summ < 10:
      left += 1
    else:
      return True

  return False


print(find_numbers([1, 2, 3, 10, 12, 20], 15))
