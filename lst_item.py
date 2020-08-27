def last_item():
  my_lst = [1,3,4,5,7,8]
  if(len(my_lst) == 0):
    return "empty list"
  else:
    return my_lst[-1]


print (last_item())