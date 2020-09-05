def find_largest(list1):
  # sort the list 
  list1.sort()
  return list1[-2],list1[-1]

print(find_largest([10, 20, 4, 45, 99,65]))

