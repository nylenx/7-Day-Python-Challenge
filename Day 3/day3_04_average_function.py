def make_avg(*args) -> float:
    if not args:
        return 0
    return sum(args)/len(args)

user_inputs = input("Enter numbers separated by spaces: ")

input_list = list(map(float,user_inputs.split()))

print(f'Average of {input_list} is {make_avg(*input_list)}')