students = {
    "Ana": [85, 90, 78],
    "Luis": [60, 70, 65],
    "Marta": [95, 88, 92]
}

best_average = 0
best_student = ""

for student, grades in students.items():
    average = sum(grades)/len(grades)
    print(student, (average))
    if average >= best_average:
        best_average = average
        best_student = student


print(f"The best student is {best_student} and the average grade is {best_average}")