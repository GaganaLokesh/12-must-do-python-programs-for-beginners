students=[]
n=int(input("Enter total number of students: "))

for i in range(n):
    name=input("Enter Name: ")
    marks=int(input("Enter Marks: "))

    students.append((name,marks))
# for name,marks in students:
#     if marks>=90:
#         grade="A"
#     elif marks>=75:
#         grade="B"
#     elif marks>=50:
#         grade="C"
#     else:
#         grade="Fail"
#     print(name, marks, grade)
for student in students:
    name = student[0]
    marks = student[1]
    if marks>=90:
        grade="A"
    elif marks>=75:
        grade="B"
    elif marks>=50:
        grade="C"
    else:
        grade="Fail"
    print(name, marks, grade)
