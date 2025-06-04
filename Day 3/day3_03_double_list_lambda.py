
list_len = int(input("Enter list length: "))
input_list = []

while(len(input_list)<list_len):
    input_list.append(int(input("=> ")))


print(*map(lambda x: x*2,input_list))