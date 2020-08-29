def is_palindrom(text):
    old_text = text
    new_text = text[::-1]
    if(old_text == new_text):
        return "text entered is a palindrome"
    else:
        return "text entered is not a palindrome"


txt_to_check = is_palindrom(input("enter string to be reversed-->"))
print(txt_to_check)