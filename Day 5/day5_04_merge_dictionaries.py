def dict_input(count: int) -> dict:
    user_dict = {}
    for i in range(count):
        print("\nItem details")
        t_key = input("Enter key: ")
        t_val = input("Enter value: ")
        user_dict[t_key] = t_val

    return user_dict

def show_dict(inp_dict:dict):
    print('\n')
    for x, y in inp_dict.items():
        print(x, y)


first_dict_el = int(input("Enter Dict 1 element no: "))
dict_input1 = dict_input(first_dict_el)
show_dict(dict_input1)

Second_dict_el = int(input("Enter Dict 2 element no: "))
dict_input2 = dict_input(Second_dict_el)
show_dict(dict_input2)

dict_input1.update(dict_input2)

print("\nMerged Dict")
show_dict(dict_input1)
