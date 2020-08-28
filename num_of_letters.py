def check_string(the_txt, a):
  num_of_occurence = 0
  for char in the_txt:
    if(char == a):
      num_of_occurence = num_of_occurence + 1
      print(num_of_occurence)
    # print (num_of_occurence)


do_the_txt = input("enter text-->")
a = input("what text? --> ")
check_string(do_the_txt, a)
# print (do_the_txt)