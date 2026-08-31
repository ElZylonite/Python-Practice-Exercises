students = {
    "Ana": [85, 90, 78],
    "Luis": [60, 70, 65],
    "Marta": [95, 88, 92]
}


for student, grades in students.items():
    average = sum(grades)/len(grades)
    print(student, float(average))