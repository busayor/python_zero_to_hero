def triple_filter(nums):
  res = list(filter(lambda x:(x % 4 == 0), nums))
  # if res:
  #   new_res = 1
  #   for num in res:
  #     new_res = list(num * 3)
  #   print(new_res)
  print("Numbers divisible by 4 are",res)


triple_filter([12, 65, 54, 8, 39, 102, 339, 20,])
  