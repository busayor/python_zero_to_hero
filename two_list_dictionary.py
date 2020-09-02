def two_list_dict(l1,l2):
  d = {k:v for k,v in zip(l1,l2)}
  return d

print(two_list_dict(['name','age','sex'],['fola',23,'male']))