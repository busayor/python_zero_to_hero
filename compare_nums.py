def compare_nums(a,b):
  if(a>b):
    print(f'{a} is greater than {b}')
  elif (b > a):
    print(f'{b} is greater than {a}')
  else:
    print(f'{a} and {b} are the same')


a = int(input("enter first num -->"))
b = int(input("enter second num -->"))
print(compare_nums(a,b))