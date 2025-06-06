def multiple_input() -> list:
    input_str = input('Enter values separated by spaces:\n--> ')
    return set(map(str,input_str.split()))

user_input1 = multiple_input()

user_input2 = multiple_input()

print(f'Union => ',user_input1|user_input2)
print(f'Intersection => ',user_input1&user_input2)

