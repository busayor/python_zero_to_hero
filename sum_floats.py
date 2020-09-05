def sum_floats(nums):
  return (sum([i for i in nums if isinstance(i, float)]))

print(sum_floats(['a',1,'f',3.2,4,3.25]))