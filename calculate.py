def calculate(opp,a,b,make_int,msg):
  if opp == '+':
    if make_int == 0:
      sum = int(a+b)
    else:
      sum = a + b
    if msg == 'n':
      return "The result is: ", sum
    else: 
      return "I got: ", sum
  elif opp == '-':
    if make_int == 0:
      diff = int(a-b)
    else:
      diff = a-b
    if msg == 'n':
      return "The result is: ", diff
    else: 
      return "I got: ", diff
  elif opp == '*':
    if make_int == 0:
      mult = int(a*b)
    else:
      mult = a*b
    if msg == 'n':
      return "The result is: ", mult
    else: 
      return "I got: ", mult
  elif opp == '/':
    if make_int == 0:
      div = int(a/b)
    else:
      div = a / b
    if msg == 'n':
      return "The result is: ", div
    else: 
      return "I got: ", div
  else:
    return None

#first two numbers are for vars a and b
#the third num is for make_int
opp = input("enter one of these: +, -, *, / ==>")
a = int(input("enter first value ==>"))
b = int(input("enter second value ==>"))
make_int = input("enter 0 for True and 1 for False ==>")
msg = input("Use defsult message? enter n for no or y for yes ==>")
# print(calculate('+',5.1,3,0,'y'))
print(calculate(opp,a,b,make_int,msg))
  