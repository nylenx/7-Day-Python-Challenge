def is_palindrome(input_string:str) -> bool:
    input_string = input_string.lower()
    
    # # Method 1
    # for el in range(len(input_string)//2):
    #     if input_string[el] != input_string[-1-el]:
    #         return False
    # return True

    # Method 2
    return input_string[0:len(input_string)//2] == input_string[-1:-1*(len(input_string)//2+1):-1]

user_input = input('Enter to check palindrome: ')

print("It's Palindrome") if is_palindrome(user_input) else print("NOT Palindrome")