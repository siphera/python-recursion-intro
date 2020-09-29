'''
# ADDITION FUNCTION

def addition(num1, num2):
    answer = num1 + num2
    return answer


first_number = int(input("please enter first number"))
second_number = int(input("please enter second number"))
result = addition(first_number, second_number)
print(result)
'''

'''
# FACTORIAL WHILE LOOP
number = 5
factorial = 1
while number > 1:
    factorial = factorial * number
    number = number - 1
print(factorial)
'''

# FACTORIAL USING RECURSION
def fact(number):
    if number < 2:
        return 1
    else:
        result = number * fact(number - 1)
        return result


my_input = int(input("enter a number"))
print(fact(my_input))

