user_input = input("Enter file content: ")

file = open('./Day 5/sample_file.txt','w')
file.write(user_input)

file.close()

print("Reading back file =>")
file = open('./Day 5/sample_file.txt')
print(file.read())