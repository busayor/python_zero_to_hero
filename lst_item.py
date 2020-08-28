# def last_item():
#   my_lst = [1,3,4,5,7,8]
#   if(len(my_lst) == 0):
#     return "empty list"
#   else:
#     return my_lst[-1]


# print (last_item())


def last_item(myTxt):
    if(len(myTxt) == 0):
       return "empty string" 
    else:
        return myTxt[-1]


show_last_item = last_item(input("enter text here-->"))
print (show_last_item)
