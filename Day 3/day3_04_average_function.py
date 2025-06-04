no_of_input = int(input("Enter number of inputs: "))

input_list = []

while(len(input_list)<no_of_input):
    input_list.append(int(input("=> ")))

print(f'Average of {input_list} is {sum(input_list)/no_of_input}')