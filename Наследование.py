class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __lt__(self, other):
        if self.surname == other.surname:
            return self.name < other.name
        return self.surname < other.surname

    def __gt__(self, other):
        if self.surname == other.surname:
            return self.name > other.name
        return self.surname > other.surname

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
