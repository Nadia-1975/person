# class Student:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#     lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]
#     def lecturer_rating( sefe, lecturer_list, course_name):
#         sum_all = 0
#         count_all = 0
#         for student in  lecturer_list:
#             if stud.courses_in_progress == [course_name]:
#                 sum_all += stud.average_rating
#                 count_all += 1
#         average_for_all = sum_all / count_all
#         return average_for_all
#
#     def __str__(self):
#         grades_count = 0
#         courses_in_progress_string = ', '.join(self.courses_in_progress)
#         finished_courses_string = ', '.join(self.finished_courses)
#         for k in self.grades:
#             grades_count += len(self.grades[k])
#         self.average_rating = sum(map(sum, self.grades.values())) / grades_count
#         res = f'Name: {self.name}\n' \
#               f'Surname: {self.surname}\n' \
#               f'Average_rating: {self.average_rating}\n' \
#               f'Courses_in_progress_string: {courses_in_progress_string}\n' \
#               f'Finished_courses_string: {finished_courses_string}'
#         return res
#
#     def rate_hw(self, lecturer, course, grade):
#
#         if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
#             if course in lecturer.grades:
#                 lecturer.grades[course] += [grade]
#             else:
#                 lecturer.grades[course] = [grade]
#         else:
#             return 'Mistake'
#
#     def __lt__(self, other):
#
#         if not isinstance(other, Student):
#             print('This comparison is incorrect')
#             return
#         return self.average_rating < other.average_rating
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
# class Lecturer(Mentor):
#
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.grades = {}
#
#     student_list = [student_1, student_2, student_3]
#     def student_rating(self, student_list, course_name):
#         sum_all = 0
#         count_all = 0
#         for lect in lecturer_list:
#             if lect.courses_attached == [course_name]:
#                 sum_all += lect.average_rating
#                 count_all += 1
#         average_for_all = sum_all / count_all
#         return average_for_all
#
#     def __str__(self):
#         grades_count = 0
#         for k in self.grades:
#             grades_count += len(self.grades[k])
#         self.average_rating = sum(map(sum, self.grades.values())) / grades_count
#         res = f'Name: {self.name}\nSurname: {self.surname}\nAverage grade for lectures: {self.average_rating}'
#         return res
#
#     def __lt__(self, other):
#
#         if not isinstance(other, Lecturer):
#             print('This comparison is incorrect')
#             return
#         return self.average_rating < other.average_rating
#
#
# class Reviewer(Mentor):
#     def rate_hw(self, student, course, grade):
#
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Mistake'
#
#     def __str__(self):
#
#         res = f'Name: {self.name}\nSurname: {self.surname}'
#         return res
#
#
# best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
# best_lecturer_1.courses_attached += ['Python']
#
# best_lecturer_2 = Lecturer('Petr', 'Petrov')
# best_lecturer_2.courses_attached += ['Git']
#
# best_lecturer_3 = Lecturer('Semen', 'Zarev')
# best_lecturer_3.courses_attached += ['Python']
#
#
# cool_reviewer_1 = Reviewer('Some', 'Buddy')
# cool_reviewer_1.courses_attached += ['Python']
# cool_reviewer_1.courses_attached += ['Git']
#
# cool_reviewer_2 = Reviewer('Ostap', 'Bender')
# cool_reviewer_2.courses_attached += ['Python']
# cool_reviewer_2.courses_attached += ['Git']
#
#
# student_1 = Student('Denis', 'Sviridov')
# student_1.courses_in_progress += ['Python']
# student_1.finished_courses += ['Introduction to Programming']
#
# student_2 = Student('Roman', 'Malikov')
# student_2.courses_in_progress += ['Git']
# student_2.finished_courses += ['Introduction to Programming']
#
# student_3 = Student('Sidor', 'Petrov')
# student_3.courses_in_progress += ['Python']
# student_3.finished_courses += ['Introduction to Programming']
#
#
# student_1.rate_hw(best_lecturer_1, 'Python', 10)
# student_1.rate_hw(best_lecturer_1, 'Python', 10)
# student_1.rate_hw(best_lecturer_1, 'Python', 10)
#
# student_1.rate_hw(best_lecturer_2, 'Python', 5)
# student_1.rate_hw(best_lecturer_2, 'Python', 7)
# student_1.rate_hw(best_lecturer_2, 'Python', 8)
#
# student_1.rate_hw(best_lecturer_1, 'Python', 7)
# student_1.rate_hw(best_lecturer_1, 'Python', 8)
# student_1.rate_hw(best_lecturer_1, 'Python', 9)
#
# student_2.rate_hw(best_lecturer_2, 'Git', 10)
# student_2.rate_hw(best_lecturer_2, 'Git', 8)
# student_2.rate_hw(best_lecturer_2, 'Git', 9)
#
# student_3.rate_hw(best_lecturer_3, 'Python', 5)
# student_3.rate_hw(best_lecturer_3, 'Python', 6)
# student_3.rate_hw(best_lecturer_3, 'Python', 7)
#
#
# cool_reviewer_1.rate_hw(student_1, 'Python', 8)
# cool_reviewer_1.rate_hw(student_1, 'Python', 9)
# cool_reviewer_1.rate_hw(student_1, 'Python', 10)
#
# cool_reviewer_2.rate_hw(student_2, 'Git', 8)
# cool_reviewer_2.rate_hw(student_2, 'Python', 7)
# cool_reviewer_2.rate_hw(student_2, 'Introduction to Programming', 9)
#
# cool_reviewer_2.rate_hw(student_3, 'Python', 8)
# cool_reviewer_2.rate_hw(student_3, 'Python', 7)
# cool_reviewer_2.rate_hw(student_3, 'Python', 9)
# cool_reviewer_2.rate_hw(student_3, 'Python', 8)
# cool_reviewer_2.rate_hw(student_3, 'Python', 7)
# cool_reviewer_2.rate_hw(student_3, 'Python', 9)
#
#
#
#
#
# print()
# print(f'LIST OF VERIFIERS:\n\n{cool_reviewer_1}\n\n{cool_reviewer_2}')
# print()
# print(f'LIST OF STUDENTS:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
# print()
# print(f'LIST OF LECTURERS:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
# print()
#
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def student_rating(student_list, course_name):
        sum_all = 0
        count_all = 0
        for stud in student_list:
            if stud.courses_in_progress == [course_name]:
                sum_all += stud.average_rating
                count_all += 1
        average_for_all = sum_all / count_all
        return average_for_all

    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Name: {self.name}\n' \
              f'Surname: {self.surname}\n' \
              f'Average_rating: {self.average_rating}\n' \
              f'Courses_in_progress_string: {courses_in_progress_string}\n' \
              f'Finished_courses_string: {finished_courses_string}'
        return res

    def rate_hw(self, lecturer, course, grade):

        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Mistake'

    def __lt__(self, other):

        if not isinstance(other, Student):
            print('This comparison is incorrect')
            return
        return self.average_rating < other.average_rating

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def lecturer_rating(lecturer_list, course_name):
        sum_all = 0
        count_all = 0
        for lect in lecturer_list:
            if lect.courses_attached == [course_name]:
                sum_all += lect.average_rating
                count_all += 1
        average_for_all = sum_all / count_all
        return average_for_all

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Name: {self.name}\nSurname: {self.surname}\nAverage grade for lectures: {self.average_rating}'
        return res

    def __lt__(self, other):

        if not isinstance(other, Lecturer):
            print('This comparison is incorrect')
            return
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):

        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Mistake'

    def __str__(self):

        res = f'Name: {self.name}\nSurname: {self.surname}'
        return res


best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Git']

best_lecturer_3 = Lecturer('Semen', 'Zarev')
best_lecturer_3.courses_attached += ['Python']


cool_reviewer_1 = Reviewer('Some', 'Buddy')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Git']

cool_reviewer_2 = Reviewer('Ostap', 'Bender')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Git']


student_1 = Student('Denis', 'Sviridov')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Introduction to Programming']

student_2 = Student('Roman', 'Malikov')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Introduction to Programming']

student_3 = Student('Sidor', 'Petrov')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Introduction to Programming']


student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_1.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Python', 5)
student_1.rate_hw(best_lecturer_2, 'Python', 7)
student_1.rate_hw(best_lecturer_2, 'Python', 8)

student_1.rate_hw(best_lecturer_1, 'Python', 7)
student_1.rate_hw(best_lecturer_1, 'Python', 8)
student_1.rate_hw(best_lecturer_1, 'Python', 9)

student_2.rate_hw(best_lecturer_2, 'Git', 10)
student_2.rate_hw(best_lecturer_2, 'Git', 8)
student_2.rate_hw(best_lecturer_2, 'Git', 9)

student_3.rate_hw(best_lecturer_3, 'Python', 5)
student_3.rate_hw(best_lecturer_3, 'Python', 6)
student_3.rate_hw(best_lecturer_3, 'Python', 7)


cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)
cool_reviewer_1.rate_hw(student_1, 'Python', 10)

cool_reviewer_2.rate_hw(student_2, 'Git', 8)
cool_reviewer_2.rate_hw(student_2, 'Python', 7)
cool_reviewer_2.rate_hw(student_2, 'Introduction to Programming', 9)

cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)
cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)


student_list = [student_1, student_2, student_3]
lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

print()
print(f'LIST OF VERIFIERS:\n\n{cool_reviewer_1}\n\n{cool_reviewer_2}')
print()
print(f'LIST OF STUDENTS:\n\n{student_1}\n\n{student_2}\n\n{student_3}')
print()
print(f'LIST OF LECTURERS:\n\n{best_lecturer_1}\n\n{best_lecturer_2}\n\n{best_lecturer_3}')
print()

