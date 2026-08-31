name = ["Adrian", "Eric", "Juan"]
grade = [70, 90, 50]

graded_papers = list(zip(name, grade))
best_grade = 0

for n, g in graded_papers:
    if g > best_grade:
        best_grade = g
        name_best_grade = n


print(name_best_grade, best_grade)