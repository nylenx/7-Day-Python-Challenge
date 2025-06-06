def multiple_input() -> list:
    input_str = input('Enter values separated by spaces:\n--> ')
    return list(map(str,input_str.split()))

def show_list(the_list: list):
    print('=> ', *the_list)

user_input = multiple_input()

show_list(user_input)

user_input = list(set(user_input))

print("After removing duplicate using set ")
show_list(user_input)