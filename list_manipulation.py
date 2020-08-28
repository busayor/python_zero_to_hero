fruits = ['mango', 'apple', 'grape', 'banana']
def list_manipulation(newItem,new_fruit_loc,action):
    if(action == 1):
        if(new_fruit_loc == 'e'):
            fruits.append(newItem)
            print(fruits)
        elif(new_fruit_loc == 'b'):
            fruits.insert(0,newItem)
            print(fruits)
        else:
            print(f"Wrong text entered, {fruits} still remains the same")
    elif(action == 0):
        if(new_fruit_loc == 'e'):
            fruits.pop()
            print(fruits)
        elif(new_fruit_loc == 'b'):
            fruits.pop(0)
            print(fruits)
        else:
            print(f"Wrong text entered, {fruits} still remains the same")
    else:
        print(f"Invalid selection")

action = int(input("Would you like to add/remove an item? enter 0 to remove and 1 to add -->"))
newFruit = input("Enter a new item to the list -->")
new_fruit_loc = input("Enter location, b or beginning, e for end -->")
list_manipulation(newFruit,new_fruit_loc,action)
# print(len(fruits))