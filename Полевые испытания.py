def avg_grade_for_course(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    return total_grade / count if count != 0 else 0

def avg_lecture_grade_for_course(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total_grade / count if count != 0 else 0

# Создаем экземпляры классов
student1 = Student('John', 'Doe', 'male')
student2 = Student('Jane', 'Smith', 'female')
lecturer1 = Mentor('Mark', 'Johnson')
lecturer2 = Mentor('Sarah', 'Williams')

# Вызываем методы
student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer1, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 8)

lecturer1.rate_hw(student1, 'Python', 10)
lecturer1.rate_hw(student2, 'Python', 9)
lecturer2.rate_hw(student1, 'Python', 8)
lecturer2.rate_hw(student2, 'Python', 7)

# Выводим результаты
print(f"Средняя оценка за домашние задания по курсу Python: {avg_grade_for_course([student1, student2], 'Python')}")
print(f"Средняя оценка за лекции по курсу Python: {avg_lecture_grade_for_course([lecturer1, lecturer2], 'Python')}")
