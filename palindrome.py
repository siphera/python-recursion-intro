def palindrome(input_str):
    if len(input_str) <= 1:
        return True
    else:
        return input_str[0] == input_str[-1] and palindrome(input_str[1: -1])


input_string = input("please enter a string or number: ")
print(palindrome(input_string))

