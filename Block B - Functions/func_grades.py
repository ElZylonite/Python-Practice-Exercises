def grades_menu():
    print("""<------ Grades Menu ------>

            1. Add grade
            2. View grades
            3. Calculate average
            4. View highest grade
            5. Exit
          """)
def add_grade(student_name, student_grade, all_grades):
    if student_grade < 0 or student_grade > 100:
        raise ValueError("Grade must be between 0 and 100.")
    all_grades.append((student_name, student_grade))
    return all_grades

def calculate_average(all_grades):
    if not all_grades:
        return 0
    average = sum(grade for _, grade in all_grades) / len(all_grades)
    return average
def view_grades(all_grades):
    if not all_grades:
        print("There is no grade data available.")
    else:
        print(f"{all_grades}")
def highest_grade(all_grades):
    if not all_grades:
        return None
    highest = max(all_grades, key=lambda x: x[1])
    return highest


all_grades = []
while True:
    grades_menu()
    action = int(input("Please select an option (1-5): "))
    

    if action == 1:
        student_name = input("Enter the student's name: ")
        student_grade = float(input("What is the student's grade? "))
        add_grade(student_name, student_grade, all_grades)
        print(f"Added {student_name} with grade {student_grade}.")
    elif action == 2:
        view_grades(all_grades)
    elif action == 3:
        average = calculate_average(all_grades)
        print(f"The average grade is: {average}")
    elif action == 4:
        highest = highest_grade(all_grades)
        if highest:
            print(f"The highest grade is: {highest[0]} with a grade of {highest[1]}")
        else:
            print("There is no grade data available.")
    elif action == 5:
        print("Exiting the grades menu. Goodbye!")
        break
       