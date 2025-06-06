def multiple_input() -> list:
    input_str = input('Enter values separated by spaces:\n--> ')
    return tuple(map(str,input_str.split()))

user_input = multiple_input()

print('Tuple => ',*user_input)
print('\nUnpacked tuple: ')
(var1,var2,var3) = user_input

print(f'var1 = {var1}\nvar2 = {var2}\nvar3 = {var3}')