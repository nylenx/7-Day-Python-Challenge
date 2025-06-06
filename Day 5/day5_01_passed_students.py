def dict_input(count: int) -> dict:
    user_dict = {}
    for i in range(count):
        print("\nStudent details")
        t_key = input("Enter name: ")
        t_val = int(input("Enter score: "))
        user_dict[t_key] = t_val
        # print(*user_dict)

    return user_dict

stud_num = int(input("Enter number of student to enter: "))
student_rec = dict_input(stud_num)

print("All Students =>", *student_rec,"\nStudent passed :")


for name, score in student_rec.items():
    if score >40:
        print(name)