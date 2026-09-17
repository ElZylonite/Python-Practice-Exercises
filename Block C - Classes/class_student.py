class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def highest_grade(self):
        highest = self.grades[0]
        for grade in self.grades:
            if grade > highest:
                highest = grade
        return highest

ana = Student("Ana")
ana.add_grade(85)
ana.add_grade(90)
ana.add_grade(78)
print(ana.highest_grade())