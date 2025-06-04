print('For basic Calculations please enter two valid operands: ')
first_operand = float(input("First Operand: "))
second_operand = float(input("Second Operand: "))


operator = input("Enter operator:  + (Addition), - (Subtraction), * (Multiplication), / (Division), % (remainder)\n=> ")

if operator == '+':
    print(f'{first_operand} {operator} {second_operand} = {first_operand+second_operand}')
elif operator == '-':
    print(f'{first_operand} {operator} {second_operand} = {first_operand-second_operand}')
elif operator == '*':
    print(f'{first_operand} {operator} {second_operand} = {first_operand*second_operand}')
elif operator == '/':
    print(f'{first_operand} {operator} {second_operand} = {first_operand/second_operand}')
elif operator == '%':
    print(f'{first_operand} {operator} {second_operand} = {first_operand%second_operand}')
else:
    print("Invalid input")





