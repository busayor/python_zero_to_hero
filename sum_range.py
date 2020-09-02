def sum_range(end, strt):
  sum = 0
  for num in range(strt, end):
    sum = sum + num
  return sum


print(sum_range(20,1))