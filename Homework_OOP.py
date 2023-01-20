class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def calc_average(self):
        average = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return average

    def __str__(self):
        some_student = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.calc_average()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return some_student

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Not a Student'
        return self.calc_average() < other.calc_average()

student1 = Student('Анна', 'Николаева', 'ж')
student1.finished_courses += ['Компьютерная грамотность', 'Основы программирования']
student1.courses_in_progress += ['Git', 'Основы Python']
student2 = Student('Александр', 'Абрамов', 'ж')
student2.finished_courses += ['Основы программирования', 'Английский для IT-специалистов']
student2.courses_in_progress += ['Основы Python', 'Git']

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def calc_average(self):
        average = sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), []))
        return average

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.calc_average()}'
        return some_reviewer

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a Lecturer'
        return self.calc_average() < other.calc_average()

lecturer1 = Lecturer('Ирина', 'Старцева')
lecturer1.courses_attached += ['Основы Python', 'Компьютерная грамотность', 'Git']
lecturer2 = Lecturer('Елена', 'Никифорова')
lecturer2.courses_attached += ['Git', 'Английский для IT-специалистов', 'Основы программирования', 'Основы Python']

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_reviewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_reviewer

reviewer1 = Reviewer('Мария', 'Ветрова')
reviewer1.courses_attached += ['Основы Python', 'Git']
reviewer2 = Reviewer('Роман', 'Петров')
reviewer2.courses_attached += ['Git', 'Основы Python']

student1.rate_lecturer(lecturer1, 'Основы Python', 9)
student1.rate_lecturer(lecturer1, 'Git', 8)
student1.rate_lecturer(lecturer2, 'Основы Python', 10)
student1.rate_lecturer(lecturer2, 'Git', 6)
student2.rate_lecturer(lecturer1, 'Основы Python', 9)
student2.rate_lecturer(lecturer1, 'Git', 10)
student2.rate_lecturer(lecturer2, 'Основы Python', 8)
student2.rate_lecturer(lecturer2, 'Git', 7)

reviewer1.rate_hw(student1, 'Основы Python', 9)
reviewer1.rate_hw(student2, 'Основы Python', 6)
reviewer1.rate_hw(student1, 'Git', 7)
reviewer1.rate_hw(student2, 'Git', 8)
reviewer2.rate_hw(student1, 'Основы Python', 8)
reviewer2.rate_hw(student2, 'Основы Python', 10)
reviewer2.rate_hw(student1, 'Git', 10)
reviewer2.rate_hw(student2, 'Git', 9)

students_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]

def av_grade_student(course, list=students_list):
    sum_grades = 0
    len_grades = 0
    for student in list:
        if course in student.grades:
            sum_grades += sum(student.grades[course])
            len_grades += len(student.grades[course])
        else:
            return 'Нет такого курса'
    return f'Средний балл студентов за курс {course}: {sum_grades / len_grades}'

def av_grade_lecturer(course, list=lecturer_list):
    sum_grades = 0
    len_grades = 0
    for lecturer in list:
        if course in lecturer.grades:
            sum_grades += sum(lecturer.grades[course])
            len_grades += len(lecturer.grades[course])
        else:
            return 'Нет такого курса'
    return f'Средний балл лекторов за курс {course}: {sum_grades / len_grades}'

print(reviewer1)
print(reviewer2)
print()
print(lecturer1)
print(lecturer2)
print()
print(student1)
print(student2)
print()
print(student1 < student2)
print(lecturer2 < lecturer1)
print()
print(av_grade_student('Git'))
print(av_grade_student('Основы Python'))
print()
print(av_grade_lecturer('Git'))
print(av_grade_lecturer('Основы Python'))










