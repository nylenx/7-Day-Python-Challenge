first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

third_variable = input("Using Third variable Y/N (YES/NO): ")

print(f'\nThis is first number : {first_number} & second number {second_number}')

if third_variable.upper() == 'Y':
    # Swapping the numbers using a temporary variable
    temp_var = first_number
    first_number = second_number
    second_number = temp_var
    print(f'\nSame output after swapping (WITH third variable),\nThis is first number : {first_number} & second number {second_number}')
else:
    # Swapping the numbers without temporary variable
    temp_var = first_number
    first_number = second_number
    second_number = temp_var
    print(f'\nSame output after swapping (WITHOUT third variable),\nThis is first number : {first_number} & second number {second_number}')


