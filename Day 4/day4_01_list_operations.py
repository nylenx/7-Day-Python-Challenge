def show_list(the_list: list):
    print('=> ', *the_list)

def single_input() -> str:
    input_str = input("Enter single item:\n--> ")
    return input_str

def multiple_input() -> list:
    input_str = input('Enter values separated by spaces:\n--> ')
    return list(map(str,input_str.split()))
     

def end_insert(the_list: list ) -> list:
    try:
        value = single_input()
        the_list.append(value)
        print(f'Item added at End -> {value}')
    except Exception as e:
        print(e)
    finally:
        show_list(the_list)
        return the_list

def index_insert(the_list: list) -> list:
    try:
        ind = int(input("Insert index:\n=> "))
        value = single_input()
        the_list.insert(ind,value)
        print(f'Item added @ {ind} -> {value}')
    except Exception as e:
        print(e)
    finally:
        show_list(the_list)
        return the_list
    
def multi_insert(the_list: list) -> list:
    try:
        multi_elm = multiple_input()
        for elm in multi_elm:
            the_list.append(elm)
        print(f'Item added multiple -> ',*multi_elm)
    except Exception as e:
        print(e)
    finally:
        show_list(the_list)
        return the_list
    
def end_remove(the_list: list) -> list:
    try:
        the_list.pop()
        print(f'Last Item removed')
    except Exception as e:
        print(e)
    finally:
        show_list(the_list)
        return the_list
    
def value_remove(the_list: list) -> list:
    try:
        value = single_input()
        the_list.remove(value)
        print(f'Item removed -> {value}')
    except Exception as e:
        print(e)
    finally:
        show_list(the_list)
        return the_list
    
def index_remove(the_list: list) -> list:
    try:
        ind = int(input("Remove index:\n=> "))
        the_list.pop(ind)
        print(f'Item removed @ {ind}')
    except Exception as e:
        print(e)
    finally:
        show_list(the_list)
        return the_list
    
def all_remove(the_list: list) -> list:
    try:
        the_list.clear()
        print('List Cleared...')
    except Exception as e:
        print(e)
    finally:
        show_list(the_list)
        return the_list
    
if __name__ == '__main__':
    loop = True
    crud_list = []
    show_list(crud_list)
    print('''
1. Insert at END
2. Insert by INDEX
3. Multi-Insert
4. Remove last
5. Remove by VALUE
6. Remove by INDEX
7. Clear List
8. Preview List
0.Exit''')
    while(loop):
        option = input('''
List CRUD operation
__________________________\n 
-- > ''')
        if option == '1':
            end_insert(crud_list)
            continue
        elif option == '2':
            index_insert(crud_list)
            continue
        elif option == '3':
            multi_insert(crud_list)
            continue
        elif option == '4':
            end_remove(crud_list)
            continue
        elif option == '5':
            value_remove(crud_list)
            continue
        elif option == '6':
            index_remove(crud_list)
            continue
        elif option == '7':
            all_remove(crud_list)
            continue
        elif option == '8':
            show_list(crud_list)
            continue
        elif option == '0':
            exit()
            break
        else:
            print("INVALID INPUT, try again...")
            continue

