from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_limit(self):
        pass

class StudentUser(User):
    def get_limit(self):
        return 3

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__courses = []  

    def add_course(self, course):
        if course not in self.__courses:
            self.__courses.append(course)

    def remove_course(self, course):
        if course in self.__courses:
            self.__courses.remove(course)

    def get_courses(self):
        return self.__courses

class Course:
    def __init__(self, title, max_students):
        self.title = title
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if student not in self.students and len(self.students) < self.max_students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

class Manager:
    def register_student(self, student, course):
        user = StudentUser(student.name)

        if len(student.get_courses()) >= user.get_limit():
            print(f"[LIMIT] {student.name} kurs limitiga yetdi!")
            return

        if len(course.students) >= course.max_students:
            print(f"[FULL] {course.title} kursi tolib bolgan!")
            return

        course.add_student(student)
        student.add_course(course)
        print(f"[OK] {student.name} -> {course.title} kursiga yozildi")

    def unregister_student(self, student, course):
        course.remove_student(student)
        student.remove_course(course)
        print(f"[DEL] {student.name} -> {course.title} kursidan ochirildi")


print("---1-TEST: Student va Course yaratish---")
s1 = Student("Ali", 1)
s2 = Student("Vali", 2)

c1 = Course("Python", 2)
c2 = Course("Django", 2)
c3 = Course("AI", 2)

print("Studentlar va kurslar yaratildi")

print("---2-TEST: Royxatdan otkazish---")
manager = Manager()
manager.register_student(s1, c1)
manager.register_student(s1, c2)
print()

print("---3-TEST: Limit tekshiruvi---")
manager.register_student(s1, c3)
manager.register_student(s1, c3)
print()

print("---4-TEST: Kursdagi talabalar---")
print("Python kursi talabalari:")
for s in c1.students:
    print(s.name)
print()

print("---5-TEST: Talabaning kurslari---")
print("Ali yozilgan kurslar:")
for c in s1.get_courses():
    print(c.title)
print()

print("---6-TEST: Kursdan ochirish---")
manager.unregister_student(s1, c1)

print("Ali kurslari (ochirgandan keyin):")
for c in s1.get_courses():
    print(c.title)