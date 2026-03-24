students=[]
n=int(input("Enter total number of students: "))

for i in range(n):
    name=input("Enter Name: ")
    marks=int(input("Enter Marks: "))

    students.append((name,marks)) #tuple
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

# 🔹 Indexing happens in TWO levels ⚡
# ✅ Level 1 → List indexing
# students[0] → ("Gagana", 95)
# students[1] → ("Rahul", 80)

# 👉 Each index gives one tuple

# ✅ Level 2 → Tuple indexing

# Now inside each tuple:

# student = ("Gagana", 95)

# student[0] → "Gagana"
# student[1] → 95